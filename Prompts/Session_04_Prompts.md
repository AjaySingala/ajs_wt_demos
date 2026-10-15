# SESSION 4 - PROBLEM SOLVING & PROTOTYPING WITH GENAI
## Common

### Vague request vs. testable problem

**Vague:**
Build something that prioritizes operational tickets.

**Testable:**
Create a deterministic Python function that evaluates a ticket using documented severity and SLA rules, returns an explainable classification, identifies whether escalation is required, and handles invalid or missing inputs explicitly.

### Demo 1: Use Copilot Chat to clarify the problem
Act as a senior business analyst and solution designer.

WinTrust wants to create a small Python prototype for
deterministic operational ticket triage.

The prototype should evaluate ticket information and
produce an explainable triage result.

Do not write code yet.

First, turn the request into a problem definition containing:

1. Business problem
2. Intended users
3. Required inputs
4. Proposed outputs
5. Business rules that must be confirmed
6. Error and exception scenarios
7. Security and operational constraints
8. Acceptance criteria
9. Decisions that require human approval

Clearly distinguish:
- Requirements established by the request
- Assumptions that need confirmation
- Questions that cannot be answered from the information provided

Do not invent WinTrust policies or SLA thresholds.

Finish with the five most important questions that must
be resolved before implementation.


~~### Demo 1: Problem framing~~

~~**Prompt:**~~
~~Convert this ambiguous business problem into a structured problem statement. Identify stakeholders, current pain, root-cause hypotheses, constraints, evidence required, solution options, risks and success measures.~~

### Demo 2A: Ask Copilot Chat to review the design

Open:
`ticket_triage_starter.py`

**Prompt:**
Act as a senior Python solution architect.

Review the proposed deterministic ticket-triage design.

Input model:
Ticket(
    ticket_id,
    customer_criticality,
    severity,
    elapsed_minutes,
    sla_minutes,
    affected_transactions,
    symptom
)

Training rules:
- P1 tickets must be escalated.
- Tickets are SLA-breached when elapsed_minutes is
  strictly greater than sla_minutes.
- A ticket exactly at the SLA limit is not breached.
- Unsupported severity and invalid time values must
  be rejected.
- The output must explain the classification.
- No external action or system modification is allowed.

Do not write the implementation yet.

Provide:
1. A decision table
2. Input-validation requirements
3. Boundary cases
4. Expected output fields
5. At least eight test scenarios
6. Potential ambiguity or design risks

Use only the rules supplied above.
Do not introduce additional escalation rules based on
customer criticality, affected transaction count, or symptom.

Clearly identify any remaining design decisions.

### Demo 2B: GitHub Copilot | Implement the prototype
Implement the ``classify_ticket` function in the open file
`Code/ticket_triage_starter.py`.

Use the existing Ticket dataclass.

Implement only these training rules:

1. Severity P1 requires escalation.
2. An SLA breach occurs when elapsed_minutes is strictly
   greater than sla_minutes.
3. An SLA-breached ticket requires escalation.
4. A ticket exactly at the SLA limit is not breached.
5. Reject an unsupported severity.
6. Reject invalid time values, including negative elapsed
   time and non-positive SLA limits.
7. Reject negative affected_transactions.
8. Validate that ticket_id is not blank.

Return a dictionary containing:
- ticket_id
- severity
- sla_breached
- escalate
- reasons

The reasons field must explain the rule or rules that
caused escalation. If escalation is not required,
provide an appropriate explanation.

Requirements:
- Keep the function deterministic.
- Do not use an LLM or external service.
- Do not modify external systems or send notifications.
- Do not invent additional escalation rules.
- Use clear variable names and type hints.
- Raise a clear ValueError for invalid input.
- Preserve the existing Ticket dataclass.

After implementation, explain each rule and identify
the test cases needed to verify it.

### Demo 2C: Ask GitHub Copilot to expand the tests
Open:
`Code/test_ticket_triage.py`

**Prompt:**
Expand Code/test_ticket_triage.py using pytest.

Keep the existing tests unless they conflict with the
explicit training rules.

Add tests for:

1. A P1 ticket that is within its SLA.
2. A P2 ticket that has breached its SLA.
3. A P4 ticket that is within its SLA.
4. A ticket exactly at the SLA boundary.
5. A ticket one minute beyond the SLA boundary.
6. An unsupported severity.
7. Negative elapsed time.
8. A zero or negative SLA limit.
9. A negative affected_transactions value.
10. A blank ticket_id.
11. A ticket that breaches its SLA and is P1.
12. A ticket that does not require escalation.

For valid inputs, verify the relevant output fields,
including sla_breached, escalate, and reasons.

For invalid inputs, verify that a clear ValueError is raised.

Use the exact training rules. Do not add escalation
behavior based on customer_criticality, symptom, or
affected_transactions.

Do not change the business rules to make a test pass.

Explain what each test verifies.

### Demo 3: Conduct a code review with Copilot Chat

Use:
`Code/ticket_triage_starter.py`
`Code/test_ticket_triage.py`

**Prompt:**
Act as an independent senior Python code reviewer.

Review:
- Code/ticket_triage_starter.py
- Code/test_ticket_triage.py

Use the explicit training rules as the source of truth.

Check:

1. Whether every rule is implemented.
2. Whether SLA boundary conditions are correct.
3. Whether invalid inputs are rejected consistently.
4. Whether the output structure is consistent.
5. Whether reasons accurately explain the decision.
6. Whether unsupported escalation rules have been introduced.
7. Whether tests cover normal cases, edge cases, and invalid inputs.
8. Whether any code has unintended external side effects.
9. Whether the implementation is unnecessarily complex.
10. Whether the tests could pass despite incorrect business logic.

For every issue, provide:
- File and function
- Evidence from the code or tests
- Why it matters
- Severity
- Recommended correction
- Test that would verify the correction

Do not claim to have executed the tests unless they
were actually run.

Do not change the business rules.
Prioritize correctness over stylistic preferences.

### Data track application: SQL-based data-quality investigation
#### GitHub Copilot demo: Generate SQL data-quality checks

Use:
`transactions_500.csv`

**Prompt:**
Act as a senior data engineer and SQL developer.

The WinTrust data team needs to investigate data-quality issues
in transactions_500.csv before using the data for reporting.

We want a SQL-based solution, not a Python validation function.

First:
1.	Inspect the actual CSV headers and data types if the file is available.
2.	List the confirmed columns and identify any schema assumptions.
3.	Ask for clarification if the required fields are absent.

Then help implement SQL checks for:
- Missing or blank transaction identifiers
- Missing or blank customer identifiers
- Invalid transaction dates in YYYY-MM-DD format
- Unsupported currency codes
- Unsupported product codes
- Negative transaction amounts
- Duplicate transaction identifiers

Use these candidate allowed values only if confirmed for the exercise:
Currency codes: INR, USD, EUR
Product codes: PAY, DAT, OPS, SEC, ANL

Requirements:
- State the SQL dialect you are using.
- Do not invent columns or silently rename source fields.
- Do not invent allowed status values or other business rules.
- Make each check independently executable.
- Return the records that fail each check, along with a reason.
- Include a summary of the number of failing records per check.
- Explain how NULLs and blank strings are handled.
- Include test cases for valid records, invalid records and boundary cases.

Do not claim the SQL has been executed or validated unless it has.
Do not modify the source data. The exercise is read-only.
Start by confirming the schema and proposed approach before
generating the complete SQL solution.

### Challenge the generated SQL
Review the SQL data-quality checks you generated.

Check for:
1.	Incorrect or invented column names
2.	Incorrect handling of NULL and blank values
3.	Invalid date handling, including impossible calendar dates
4.	Duplicate detection that produces misleading counts
5.	Incorrect treatment of negative, NULL or non-numeric amounts
6.	Hard-coded allowed values that lack approval
7.	Queries that flag records incorrectly or miss invalid records
8.	SQL dialect incompatibilities
9.	Unnecessary modification of source data

For every issue:
- Show the relevant SQL
- Explain the problem
- Provide a corrected query or expression
- Give a test record that would expose the problem

Distinguish issues you can establish from the SQL itself from
issues that require execution against the dataset.

Do not claim that the queries passed tests unless they were run
and their results were inspected.

### Hands-on prompt: Enterprise Operations (not shared)

Implement the function classify_ticket in Code/ticket_triage_starter.py.

Use the existing Ticket dataclass and follow these explicit training rules:
1.	Severity P1 requires escalation.
2.	An SLA breach occurs when elapsed_minutes is strictly greater than sla_minutes.
3.	An SLA-breached ticket requires escalation.
4.	A ticket exactly at the SLA limit is not breached.
5.	Reject unsupported severity values.
6.	Reject negative elapsed time and non-positive SLA limits.
7.	Reject negative affected_transactions.
8.	Reject a blank ticket_id.

Return a dictionary containing:
- ticket_id
- severity
- sla_breached
- escalate
- reasons

The reasons field must explain the rule or rules that caused escalation. If escalation is not required, provide an appropriate explanation.

Requirements:
- Keep the function deterministic.
- Do not use an LLM or external service.
- Do not modify external systems or send notifications.
- Do not invent additional escalation rules.
- Use clear variable names and type hints.
- Raise a clear ValueError for invalid input.
- Preserve the existing Ticket dataclass.

Then expand Code/test_ticket_triage.py to cover normal cases, P1 escalation, SLA breaches, the exact SLA boundary, invalid severity, invalid time values, and blank identifiers.

Explain the implementation and tests. Do not change business rules to make a test pass.

### Hands-on prompt: Data (not shared)

You are helping the WinTrust data team investigate transaction
data quality using SQL.

Use transactions_500.csv.

First confirm the actual schema. Do not assume columns exist
until they have been verified.

Build SQL checks for:
- Missing or blank transaction and customer identifiers
- Invalid dates
- Unsupported currency and product codes, using only approved
values supplied for the exercise
- Negative transaction amounts
- Duplicate transaction identifiers

For each check:
1.	Return the affected records.
2.	Include a clear reason for each finding.
3.	Provide a summary count.
4.	Explain NULL and blank-value handling.
5.	Suggest test records for validating the query.

Requirements:
- State the SQL dialect.
- Do not invent columns, allowed status values or business rules.
- Do not update or delete source records.
- Identify any rule that cannot be implemented because its
specification is incomplete.
- Do not claim execution or correctness without evidence.

After generating the SQL, review it for boundary cases,
false positives, false negatives and dialect compatibility.

Provide a short checklist for manually validating the results.


### Additional Demo: GitHub Copilot as a technical thinking partner

Open:
`ticket_triage_starter.py`

Prompt:
Explain this program to a senior operations analyst who is not a developer. Then identify what business rules are missing from classify_ticket().

Follow with:
Implement classify_ticket() using the supplied WinTrust SLA rules. Keep the implementation deterministic, readable and testable. Do not add external dependencies.

Then:
Generate tests for normal cases, SLA breach, critical customers, low-impact tickets and ambiguous cases.
