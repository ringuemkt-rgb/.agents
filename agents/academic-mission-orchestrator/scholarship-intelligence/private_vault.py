#!/usr/bin/env python3
"""Local encrypted document vault (AES-256-GCM, scrypt). No cloud and no MCP exposure.

Install optional, audited dependency: pip install 'cryptography>=46,<47'.
No plaintext or password is printed/logged. File output is exclusive 0600.
"""
from __future__ import annotations
import argparse
from getpass import getpass
import hashlib
import os
from pathlib import Path
import secrets

MAGIC=b"SIV1\0"
SALT_BYTES=16
NONCE_BYTES=12
MIN_PASSWORD_LENGTH=16


def _derive(password: str, salt: bytes) -> bytes:
    if len(password) < MIN_PASSWORD_LENGTH:
        raise ValueError("A frase secreta precisa ter pelo menos 16 caracteres")
    if not isinstance(salt,bytes) or len(salt)!=SALT_BYTES:
        raise ValueError("Salt inválido")
    return hashlib.scrypt(password.encode("utf-8"),salt=salt,
                          n=2**15,r=8,p=1,dklen=32,maxmem=128*1024*1024)


def seal_bytes(plaintext: bytes, password: str) -> bytes:
    from cryptography.hazmat.primitives.ciphers.aead import AESGCM
    if not isinstance(plaintext,bytes) or len(plaintext)>25_000_000:
        raise ValueError("Arquivo inválido/maior que 25 MB")
    salt=secrets.token_bytes(SALT_BYTES)
    nonce=secrets.token_bytes(NONCE_BYTES)
    key=_derive(password,salt)
    ciphertext=AESGCM(key).encrypt(nonce,plaintext,MAGIC)
    return MAGIC+salt+nonce+ciphertext


def open_bytes(blob: bytes, password: str) -> bytes:
    from cryptography.hazmat.primitives.ciphers.aead import AESGCM
    if not blob.startswith(MAGIC) or len(blob)<len(MAGIC)+SALT_BYTES+NONCE_BYTES+16:
        raise ValueError("Formato de cofre inválido")
    pos=len(MAGIC)
    salt=blob[pos:pos+SALT_BYTES]
    nonce=blob[pos+SALT_BYTES:pos+SALT_BYTES+NONCE_BYTES]
    ciphertext=blob[pos+SALT_BYTES+NONCE_BYTES:]
    return AESGCM(_derive(password,salt)).decrypt(nonce,ciphertext,MAGIC)


def safe_destination(path: str) -> Path:
    target=Path(path).expanduser().resolve()
    module=Path(__file__).resolve().parent
    if target == module or module in target.parents:
        raise ValueError("Saída privada deve ficar FORA do repositório")
    target.parent.mkdir(parents=True,exist_ok=True,mode=0o700)
    if os.name=="posix":
        os.chmod(target.parent,0o700)
    return target


def write_exclusive(path: str, data: bytes):
    target=safe_destination(path)
    flags=os.O_WRONLY|os.O_CREAT|os.O_EXCL
    if hasattr(os,"O_NOFOLLOW"):
        flags |= os.O_NOFOLLOW
    fd=os.open(str(target),flags,0o600)
    try:
        with os.fdopen(fd,"wb") as file:
            file.write(data)
            file.flush()
            os.fsync(file.fileno())
    except Exception:
        try: target.unlink()
        except OSError: pass
        raise


def main():
    p=argparse.ArgumentParser(description="Cofre local; sem conexão com nuvem")
    cmd=p.add_subparsers(dest="command",required=True)
    for action in ("seal","unseal"):
        sub=cmd.add_parser(action)
        sub.add_argument("--input",required=True)
        sub.add_argument("--output",required=True)
    a=p.parse_args()
    source=Path(a.input).expanduser().resolve()
    if not source.is_file():
        p.error("Arquivo de entrada inexistente")
    password=getpass("Frase secreta do cofre (não é senha gov.br): ")
    if a.command=="seal":
        result=seal_bytes(source.read_bytes(),password)
    else:
        print("ATENÇÃO: saída será texto claro PRIVADO; use pasta criptografada e remova após uso.")
        result=open_bytes(source.read_bytes(),password)
    write_exclusive(a.output,result)
    print("Operação local concluída. Nenhum dado enviado à nuvem.")

if __name__=="__main__":
    main()
