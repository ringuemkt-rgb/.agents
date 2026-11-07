"""Encrypted, opt-in cloud snapshots for CRIA Multi-AI memory.

Keep tokens and encryption key outside source control. Data from backups is untrusted.
No network requests occur unless a cloud-specific command is selected.
"""
from __future__ import annotations

import json
import os
import sqlite3
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

MAX_SNAPSHOT_BYTES = 20_000_000
MAX_ITEMS = 30_000
MAX_CONTENT_LENGTH = 1_200
DRIVE_API = "https://www.googleapis.com/drive/v3/files"
DRIVE_UPLOAD = "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart&fields=id%2Cname%2Cparents%2CwebViewLink"


def _fernet():
    try:
        from cryptography.fernet import Fernet
    except ImportError as exc:
        raise RuntimeError("Install the optional cryptography package: pip install cryptography") from exc
    key = os.environ.get("CRIA_MEMORY_ENCRYPTION_KEY", "")
    if not key:
        raise PermissionError("CRIA_MEMORY_ENCRYPTION_KEY missing. Generate with: python -m cria_multi_ai.cloud keygen")
    try:
        return Fernet(key.encode("ascii"))
    except (ValueError, TypeError, UnicodeError) as exc:
        raise ValueError("Invalid Fernet key") from exc


def keygen() -> str:
    """Caller must store and protect this key; never add it to GitHub or Drive."""
    from cryptography.fernet import Fernet
    return Fernet.generate_key().decode("ascii")


def snapshot(db_path: str | Path, target: str | Path) -> dict:
    """Export an encrypted, versioned logical snapshot; never copy raw SQLite files."""
    db_path, target = Path(db_path).expanduser(), Path(target).expanduser()
    if not db_path.is_file():
        raise FileNotFoundError(db_path)
    conn = sqlite3.connect(f"file:{urllib.parse.quote(str(db_path.resolve()))}?mode=ro", uri=True)
    try:
        items = conn.execute("SELECT id, source, content, embedding, model FROM chunks ORDER BY id LIMIT ?", (MAX_ITEMS + 1,)).fetchall()
    finally:
        conn.close()
    if len(items) > MAX_ITEMS:
        raise ValueError("Too many memory chunks; split into smaller backups")
    obj = {
        "schema": "cria-memory-v1",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "chunks": [{"id": r[0], "source": r[1], "content": r[2], "embedding": r[3], "model": r[4]} for r in items],
    }
    raw = json.dumps(obj, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    if len(raw) > MAX_SNAPSHOT_BYTES:
        raise ValueError("Snapshot too large")
    ciphertext = _fernet().encrypt(raw)
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("xb") as f:  # fail closed; never overwrite a prior backup
        if os.name != "nt":
            os.fchmod(f.fileno(), 0o600)
        f.write(ciphertext)
    return {"encrypted": True, "chunks": len(items), "path": str(target), "bytes": len(ciphertext)}


def restore(db_path: str | Path, source: str | Path) -> dict:
    """Import authenticated encrypted data; merge idempotently; never erase existing data."""
    from cryptography.fernet import InvalidToken
    ciphertext = Path(source).expanduser().read_bytes()
    if len(ciphertext) > MAX_SNAPSHOT_BYTES * 2:
        raise ValueError("Encrypted snapshot too large")
    try:
        data = json.loads(_fernet().decrypt(ciphertext).decode("utf-8"))
    except InvalidToken as exc:
        raise ValueError("Wrong key or modified snapshot") from exc
    if not isinstance(data, dict) or data.get("schema") != "cria-memory-v1" or not isinstance(data.get("chunks"), list):
        raise ValueError("Unrecognized snapshot schema")
    if len(data["chunks"]) > MAX_ITEMS:
        raise ValueError("Too many chunks")
    validated = []
    for item in data["chunks"]:
        if not isinstance(item, dict):
            raise ValueError("Malformed chunk")
        ident, src, content = item.get("id"), item.get("source"), item.get("content")
        if not (isinstance(ident, str) and len(ident) == 24 and all(c in "0123456789abcdef" for c in ident)):
            raise ValueError("Invalid chunk ID")
        if not (isinstance(src, str) and 0 < len(src) <= 300 and isinstance(content, str) and len(content) <= MAX_CONTENT_LENGTH):
            raise ValueError("Invalid chunk content")
        embedding, model = item.get("embedding"), item.get("model")
        if embedding is not None:
            if not isinstance(embedding, str) or len(embedding) > 100_000:
                raise ValueError("Invalid embedding data")
            vector = json.loads(embedding)
            if not isinstance(vector, list) or not 1 <= len(vector) <= 4096 or not all(isinstance(v, (int, float)) and abs(v) < 1e8 for v in vector):
                raise ValueError("Invalid embedding vector")
        if model is not None and (not isinstance(model, str) or len(model) > 120):
            raise ValueError("Invalid model name")
        validated.append((ident, src, content, embedding, model))
    # Validate EVERYTHING before opening a write transaction.
    from .core import Memory
    path = Path(db_path).expanduser()
    path.parent.mkdir(parents=True, exist_ok=True)
    memory = Memory(str(path))
    inserted = 0
    try:
        with memory.db:
            for ident, src, content, embedding, model in validated:
                cur = memory.db.execute("INSERT OR IGNORE INTO chunks(id,source,content,embedding,model) VALUES(?,?,?,?,?)", (ident, src, content, embedding, model))
                if cur.rowcount == 1:
                    memory.db.execute("INSERT INTO chunks_fts(id,content) VALUES(?,?)", (ident, content))
                    inserted += 1
    finally:
        memory.close()
    return {"restored": inserted, "already_present": len(validated) - inserted, "encrypted": True}


def _request(url: str, token: str, method: str = "GET", data: bytes | None = None, headers: dict | None = None) -> dict:
    if not token:
        raise PermissionError("GOOGLE_DRIVE_ACCESS_TOKEN missing; do not copy the ChatGPT MCP OAuth token")
    hdrs = {"Authorization": "Bearer " + token, "Accept": "application/json", **(headers or {})}
    req = urllib.request.Request(url, data=data, method=method, headers=hdrs)
    with urllib.request.urlopen(req, timeout=30) as resp:
        if resp.headers.get("Content-Type", "").startswith("application/json"):
            return json.load(resp)
        return {"content": resp.read()}


def drive_list(folder_id: str, token: str) -> list[dict]:
    if not folder_id or not folder_id.replace("-", "").replace("_", "").isalnum():
        raise ValueError("Invalid Google Drive folder ID")
    q = urllib.parse.urlencode({"q": f"'{folder_id}' in parents and trashed = false", "fields": "nextPageToken,files(id,name,mimeType,size)", "pageSize": "100"})
    # Drive lists are paged; do not silently truncate.
    items, page = [], None
    while True:
        suffix = q + (("&pageToken=" + urllib.parse.quote(page)) if page else "")
        result = _request(DRIVE_API + "?" + suffix, token)
        items.extend(result.get("files", []))
        page = result.get("nextPageToken")
        if not page:
            return items
        if len(items) > 10000:
            raise ValueError("Too many Drive objects")


def drive_upload(encrypted_file: str | Path, folder_id: str, token: str) -> dict:
    if os.environ.get("CRIA_ENABLE_DRIVE_SYNC") != "YES":
        raise PermissionError("Drive upload disabled by default; set CRIA_ENABLE_DRIVE_SYNC=YES")
    path = Path(encrypted_file).expanduser()
    if path.suffix != ".enc" or path.stat().st_size > MAX_SNAPSHOT_BYTES * 2:
        raise ValueError("Only encrypted .enc snapshots up to 40 MB can be uploaded")
    if not folder_id or not folder_id.replace("-", "").replace("_", "").isalnum():
        raise ValueError("Invalid folder ID")
    # Require authenticated ciphertext before any upload, never trust a file extension.
    try:
        from cryptography.fernet import InvalidToken
        _fernet().decrypt(path.read_bytes())
    except InvalidToken as exc:
        raise ValueError("Not a decryptable CRIA snapshot") from exc
    boundary = "criamemupload9b7f7"
    metadata = json.dumps({"name": path.name, "parents": [folder_id], "mimeType": "application/octet-stream"}).encode("utf-8")
    data = (f"--{boundary}\r\nContent-Type: application/json; charset=utf-8\r\n\r\n".encode() + metadata +
            f"\r\n--{boundary}\r\nContent-Type: application/octet-stream\r\n\r\n".encode() + path.read_bytes() + f"\r\n--{boundary}--\r\n".encode())
    result = _request(DRIVE_UPLOAD, token, "POST", data, {"Content-Type": f"multipart/related; boundary={boundary}"})
    return {"uploaded": True, "remote_id": result.get("id"), "name": result.get("name")}


def drive_download(file_id: str, token: str, target: str | Path) -> dict:
    if not file_id or not file_id.replace("-", "").replace("_", "").isalnum():
        raise ValueError("Invalid Drive file ID")
    from urllib.request import Request, urlopen
    req = Request(DRIVE_API + "/" + file_id + "?alt=media", headers={"Authorization": "Bearer " + token})
    if not token:
        raise PermissionError("GOOGLE_DRIVE_ACCESS_TOKEN missing")
    with urlopen(req, timeout=30) as resp:
        data = resp.read(MAX_SNAPSHOT_BYTES * 2 + 1)
    if len(data) > MAX_SNAPSHOT_BYTES * 2:
        raise ValueError("File too large")
    path = Path(target).expanduser()
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("xb") as f:
        if os.name != "nt":
            os.fchmod(f.fileno(), 0o600)
        f.write(data)
    return {"downloaded": len(data), "path": str(path)}


if __name__ == "__main__":
    print(keygen())
