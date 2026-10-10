# Architecture

```text
                        MISSION ORCHESTRATOR
                                |
        -------------------------------------------------
        |                 |               |              |
   ADMISSIONS         RESEARCH         FUNDING         OPS
        |                 |               |              |
 Call Analyst      Methodologist    Scholarship      Relocation
 Doc Auditor       Evidence Analyst Barema Analyst   Finance
 PcD Auditor       Measurement      Lab Fit          Logistics
        |                 |               |              |
        ------------------ EVIDENCE LEDGER --------------
                                |
                          RISK ENGINE
                                |
                     ACADEMIC INTEGRITY GATE
                                |
                       HUMAN APPROVAL GATE
                                |
                            EXECUTION
```

## Design choices

### Deterministic first

Rules, deadlines, scores, file limits, and state transitions should be deterministic whenever possible. Do not ask an LLM to decide what arithmetic or a schema can decide exactly.

### Stateful mission

Long-horizon work requires persisted state:

- current gate;
- deadlines;
- evidence ledger;
- scores;
- unresolved gaps;
- decisions;
- next actions.

### Human-in-the-loop for consequential writes

Research and drafting can be automated aggressively. External consequential actions require a gate.

### Public core / private context

The core agent is portable and public. Candidate identity, health information, credentials, live application material, and unpublished proposal text are private runtime inputs.
