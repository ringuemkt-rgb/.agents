# Privacy and Security

## Public repository rule

Do not commit real:

- CPF/SSN/national IDs;
- passport/RG/CNH numbers;
- phone/address;
- health diagnoses or reports;
- government-account data;
- passwords/tokens/API keys;
- private emails;
- application PDFs;
- scholarship declarations;
- unpublished live proposal text when public disclosure could identify an anonymous candidate.

## Public/private split

### Public core

- workflows;
- prompts;
- schemas;
- generic methods;
- checklists;
- sanitized examples.

### Private runtime context

- candidate identity;
- health/PcD records;
- documents;
- real scores;
- employment details;
- live proposal;
- correspondence;
- financial status.

## Pre-publication scan

Check for:

- email addresses;
- phone patterns;
- national IDs;
- exact street addresses;
- secrets;
- signed PDFs/images;
- QR codes/barcodes;
- metadata authorship in anonymous material.

Use a PII scanner such as Microsoft Presidio where appropriate, then perform manual QA.
