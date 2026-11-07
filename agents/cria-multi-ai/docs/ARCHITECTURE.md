# Architecture and permission gates

1. **Ingest**: explicitly supplied UTF-8 `.md`/`.txt` document, 1MB cap, chunked into SQLite locally. DB is not version controlled.
2. **Retrieve**: zero-cost FTS5 lexical search, optionally mixed with cosine similarity when **local** BAAI/bge-m3 embeddings are enabled.
3. **Reason**: no model call by default. Optional local Ollama Qwen3.5-4B or explicit Hugging Face inference token + opt-in. Citations are passed as untrusted data; no instructions from documents are executed.
4. **Verify**: unittest with lexical, semantic mock, no-inference permission tests, plus scheduled offline smoke. Adapter mock is not a real model invocation.
5. **Report**: CLI JSON with retrieval references, model identity when used, and fail-closed statuses.

## Security constraints

- Do not ingest health records, minors' personal data, payments, credentials, private corporate files into a public repository. Local SQLite is plaintext: use encrypted disk and backups for sensitive use.
- Never set `CRIA_ENABLE_HF_INFERENCE=YES` in CI. Model costs may exceed free grants; remote costs are not hard-capped by this code, so real zero-spend guarantee requires excluding remote providers.
- Do not place auth tokens in logs, prompts, docs, actions artifacts or source control.
- Read-only scheduled workflow. No automatic writes to branches, external systems or data stores. Branch and PR review required for releases.
- SQLite FTS5 can be unavailable on custom Python builds. CI verifies on GitHub runners.
- Optional BGE model weights are downloaded at first local use. This may be unsuitable for mobile devices with low RAM.
- Public demonstrations are synthetic. Never mix workspaces' private data without authorization.

## Test coverage and known limits

- Deterministic offline core and remote adapter contract tested in stdlib unittest.
- Hugging Face API and BGE-M3 inference **not live-tested** by offline CI; test separately in a permitted, funded environment.
- Scheduler checks health; it does not autonomously collect private files or modify code.
- Future milestone: encrypted local memory, per-source ACLs, model-eval fixtures, and explicit cost counters before any unattended inference.

### Cloud memory v0.2 (opt-in)

- Encrypted logical JSON snapshot, schema `cria-memory-v1`, protected by
  Fernet AES-128-CBC/HMAC-SHA256 via cryptography; key lives only in a private
  environment variable/password manager. Never save it in Git, Drive or Actions.
- SQLite remains offline-first. Import validates every chunk and uses
  `INSERT OR IGNORE`, preserving existing data and rebuilding FTS locally.
- Drive's folder is private and was verified owner-only when created.
  Cloud snapshots require `CRIA_ENABLE_DRIVE_SYNC=YES` and a device-local
  `GOOGLE_DRIVE_ACCESS_TOKEN`; no invisible upload or scheduled external writes.
- GitHub Actions keeps a pure offline mode. Current session has no official
  inference credentials and no model weights, so HF Qwen/BGE real inference
  remains pending hardware/credentials. The adapters' mocked tests are not
  proof of a real model run.
