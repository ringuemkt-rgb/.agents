# Freshness & Provenance v1.0

Every material claim should carry:
- claim_id
- source_ids
- directness
- certainty
- data state
- freshness class

Suggested TTL classes:
STATIC
MONTHS_12
DAYS_90
DAYS_30
DAYS_7
LIVE

A build produces build-manifest.json with a SHA-256 content hash so the evidence/prompt state can be reconstructed later.

For current rules, rankings, events, platform capabilities or guidelines, revalidate against the currently authoritative source before publication.
