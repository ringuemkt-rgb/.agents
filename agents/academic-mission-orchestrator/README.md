# Academic Mission Orchestrator

Portable, evidence-first operating system for long-horizon academic missions: admissions, affirmative-action compliance, research proposals, scholarship strategy, relocation, and research-program integration.

This package is designed to be loaded into ChatGPT, Claude, Gemini, Grok, local agents, or any platform that accepts system instructions or Markdown knowledge files.

## What it does

- turns a multi-month academic objective into a state machine with explicit gates;
- audits calls for applications, regulations, deadlines, and required documents;
- separates verified facts, inference, strategy, and unresolved gaps;
- builds evidence ledgers and score/barema models;
- reviews research proposals adversarially before submission;
- enforces academic-integrity and conflict-of-interest gates;
- keeps scholarship selection separate from program admission;
- plans relocation and financial transition without assuming money has arrived;
- protects PII and health information from public repositories;
- uses human approval before consequential external actions;
- supports scientific evidence synthesis and software-validation workflows.

## Fast activation

Copy the entire contents of `SYSTEM_PROMPT.md` into the target platform's system/custom-instructions field.

For a lighter setup, use `ACTIVATE.md` and attach the remaining files as knowledge.

## Privacy rule

This public package intentionally contains **no real candidate identifiers, health records, credentials, application documents, or live research proposal text**. Candidate-specific material belongs in a private context file based on `PRIVATE_CONTEXT_TEMPLATE.md`.

## Core doctrine

> Maximize the probability of crossing the next legitimate gate without damaging future gates, scientific credibility, privacy, or academic integrity.

## Files

- `SYSTEM_PROMPT.md` — canonical full activation prompt.
- `ACTIVATE.md` — compact activation prompt.
- `SKILL.md` — skills and operating procedures.
- `ARCHITECTURE.md` — internal agent architecture.
- `MISSION_STATE_MACHINE.md` — gate model.
- `EVIDENCE_PROTOCOL.md` — source and evidence rules.
- `ETHICS_COMPLIANCE.md` — academic integrity, conflict-of-interest and action gates.
- `RESEARCH_METHODS.md` — research-proposal and study-design review.
- `APPLICATION_SCHOLARSHIP_RELOCATION.md` — admissions, scholarship, finance and relocation logic.
- `COMMUNICATION_GUARDIAN.md` — email/message protocol.
- `PRIVACY_SECURITY.md` — PII and public-repo rules.
- `TOOLING.md` — recommended OSS and platform integrations.
- `PRIVATE_CONTEXT_TEMPLATE.md` — private candidate configuration template.
- `manifest.json` — machine-readable capability manifest.
- `schemas/` — state and evidence schemas.

## Non-goals

This system does not guarantee admission, scholarship awards, publication, ethics approval, or funding. It does not fabricate scores, sources, credentials, or institutional permissions. It does not send sensitive academic communications without an explicit approval gate.
