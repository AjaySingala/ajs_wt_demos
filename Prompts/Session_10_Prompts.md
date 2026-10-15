# Enterprise Ops Track - MASTER CLASS 1

## Vague prompt:

Use:
- `ops_ticket_triage_mc1_80.csv`
- `Operations_Triage_Exercise_Guide.docx`

Analyze these tickets and tell me what matters.

## Demo 1: Structured ticket triage

Tool: Copilot Chat

Use:
- `ops_ticket_triage_mc1_80.csv`
- `Operations_Triage_Exercise_Guide.docx`

**Prompt:**

Review the supplied operational tickets using the Operations Triage Exercise Guide.

For each ticket in the selected sample, return:
- Ticket ID and service
- Confirmed facts from the record
- Severity validity
- SLA breach result
- Escalation recommendation and reason codes
- Missing evidence
- Whether human review is required

For this exercise, an SLA breach occurs only when elapsed_minutes is greater than sla_target_minutes. Equality is not a breach.

Do not infer root cause from the symptom. Flag invalid records rather than silently correcting them. Do not update tickets or execute operational actions.

Show the calculations for three example tickets, including one exactly at the SLA limit. State clearly whether your analysis covers the sample or the entire dataset.

## Demo 2: Evidence-based incident reasoning

Tool: Copilot Chat

Objective: Use Copilot Chat to reason from incident evidence and a runbook without inventing a root cause.

Files: 
- `Runbook_API_Latency_Exercise.docx`
- `ops_ticket_triage_mc1_80.csv`

**Prompt:**

Using the supplied ticket records and Runbook: API Latency Investigation, prepare an incident assessment with these sections:
1.	Confirmed facts
2.	Hypotheses, clearly labelled as unconfirmed
3.	Missing evidence
4.	Safe, read-only diagnostic steps
5.	Actions requiring authorization
6.	A concise update for the incident lead

For every material conclusion, identify the supporting ticket field or runbook instruction.

Do not infer that a recent change caused the incident merely because it occurred before the symptoms. 

Do not invent operational procedures, claim that a diagnostic was executed, or recommend destructive actions without explicitly identifying the authorization requirement.

### Challenge the resasoning:
**Prompt:**

Which evidence proves that the recent change caused the incident?

### Demo 3: From operational rules to code

Objective: Demonstrate how GitHub Copilot can implement a precise operational rule specification rather than improvising business logic.

File: `Operational_Scripting_Requirements.docx`

Ask GitHub Copilot in VS Code to create ticket_triage.py and corresponding tests using the supplied requirements.

The implementation should:
- Validate required fields and numeric inputs.
- Apply the documented SLA rule: elapsed_minutes > sla_target_minutes.
- Recommend escalation for P1 tickets and SLA breaches.
- Flag invalid records for human review.
- Return a structured result with reason codes.
- Avoid network calls, ticket updates and external dependencies.

The test cases should cover the SLA boundary, a breach, P1 escalation, unsupported severity, missing ticket ID, blank description, negative elapsed time and a nonpositive SLA target.

**Prompt:**

Act as a senior Python engineer implementing a small, deterministic operational ticket-triage utility.

First, review the requirements in `Operational_Scripting_Requirements.docx`. Implement only the rules explicitly documented there. If you cannot read the DOCX directly, ask me to provide its contents rather than inventing requirements.

1. Create the implementation

Create a file named `eo_ticket_triage.py`.

Implement a function:

`triage_ticket(ticket: dict) -> dict`

The function must validate and classify one ticket record. It must not connect to external services, update tickets, execute shell commands, or perform any operational action.

2. Implement the documented rules

- A valid ticket must have a nonblank `ticket_id` and `description`.
- Supported severity values are P1, P2, P3 and P4. Flag unsupported values, including P5, for human review.
- `elapsed_minutes` must be a valid, nonnegative number.
- `sla_target_minutes` must be a valid number greater than zero.
- An SLA breach occurs only when `elapsed_minutes > sla_target_minutes`. Equality is not a breach.
- Recommend escalation for a valid P1 ticket or a valid ticket with an SLA breach.
- Invalid records must be flagged for human review. Do not silently repair invalid inputs or invent missing values.

3. Define the output contract

Return a dictionary containing:

- `ticket_id`
- `valid`
- `sla_breached`
- `escalation_recommended`
- `reason_codes`
- `human_review_required`

Use explicit reason codes, such as `P1_SEVERITY`, `SLA_BREACH`, `INVALID_SEVERITY`, `MISSING_TICKET_ID`, `BLANK_DESCRIPTION` and `INVALID_SLA_TARGET`.

Document how invalid records are represented. Do not classify an invalid record as safe merely because its SLA calculation is unavailable.

4. Create unit tests

Create `eo_test_ticket_triage.py` using Python's standard `unittest` framework.

Include tests for:
1. A valid ticket below its SLA limit.
2. A ticket exactly at its SLA limit.
3. A ticket one minute above its SLA limit.
4. A valid P1 ticket without an SLA breach.
5. An unsupported severity such as P5.
6. A missing ticket ID.
7. A blank description.
8. A negative elapsed time.
9. A zero or negative SLA target.
10. Non-numeric or missing numeric inputs.

Test both returned values and reason codes where appropriate.

5. Review before finishing

Explain the implementation, particularly:
- The SLA boundary condition.
- How invalid records are handled.
- Why the function is deterministic.
- How the tests cover boundary conditions and invalid inputs.

Do not add features beyond the requirements. Do not claim that tests have passed unless you have actually executed them. Show me the generated files and any assumptions that still require clarification.
