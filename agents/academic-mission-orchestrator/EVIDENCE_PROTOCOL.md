# Evidence Protocol

## Claim states

Use these exact labels:

- `VERIFIED_PRIMARY`
- `VERIFIED_CORROBORATED`
- `PARTIALLY_SUPPORTED`
- `INFERENCE`
- `PROPOSED`
- `UNVERIFIED`
- `CONTRADICTED`
- `EVIDENCE_GAP`

## Evidence ledger fields

Every material claim should be representable as:

- `claim_id`
- `claim`
- `state`
- `source`
- `source_date`
- `source_type`
- `supports`
- `contradicts`
- `materiality`
- `expiry_or_recheck_date`
- `notes`

## Temporal validity

Current calls, scholarship rules, staff availability, deadlines, and funding amounts are time-sensitive.

Mark facts with a recheck date when they can change.

## Contradiction policy

When two sources conflict:

1. compare authority;
2. compare publication/effective date;
3. compare whether one is a general rule and the other a specific exception;
4. do not silently reconcile;
5. record the unresolved conflict if necessary.

## Scientific evidence policy

For research claims:

- distinguish systematic reviews from primary studies;
- detect overlapping cohorts;
- do not call a publication an independent replication unless the sample is independent;
- distinguish motor, social, cognitive, physiological, feasibility, and safety outcomes;
- distinguish mechanism from clinical effect;
- report risk of bias and heterogeneity when material.
