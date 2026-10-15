# MASTER CLASS II - UNDER THE HOOD
## Common to Data + Enterprise Ops
## Grounding, retrieval, context and validation without building RAG

### Demo 1A: Ungrounded answer

Ask Copilot Chat a policy question without supplying the policy.

**Prompt:**
What caused the incident, and what should we do next?

Separate confirmed facts from assumptions. If the evidence is insufficient to determine the cause, say so.

### Demo 1B: Grounded answer
Then provide this fictional incident record:

**Incident Record:**
Incident INC-2048

10:02: Monitoring detected a sharp increase in API response time.
10:04: API error rate increased from 0.5% to 8%.
10:06: Database CPU reached 94%.
10:08: A scheduled reporting job began.
10:12: API latency remained elevated.

No database execution plan, query log or dependency trace is available.

**Prompt:**
Using only this incident record, identify:

1. Confirmed facts.
2. Plausible hypotheses.
3. Missing evidence needed to determine the root cause.
4. Safe, non-destructive diagnostic next steps.

Do not claim that the reporting job caused the incident. Do not recommend a production change without sufficient evidence.

### Demo 2A: Improve the task definition

Tool: Copilot chat.

**Prompt:**
Analyze these operational tickets and tell me what matters.

### Demo 2B: Improved Prompt
Use: `Dataset/ops_tickets_200.csv` from the existing WinTrust demo pack.

**Prompt**:
Analyze the supplied operational tickets.

Return:
- Three recurring incident patterns, if supported by the data.
- Evidence for each pattern, including ticket references and counts where available.
- Any severity or SLA concerns supported by the supplied records.
- Missing information and limitations.

Do not invent ticket fields, infer causation from correlation, or claim that you executed queries or independently verified the data.

### Demo 3: ground the answer in a runbook
Required document
- `WinTrust_Runbook_Disk_Utilization.docx`
Optional supporting documents
- `WinTrust_Operations_SLA_Policy.docx`
- `WinTrust_GenAI_Security_Guidelines.docx`

**Prompt:**
Using the supplied disk-utilization runbook, summarize the documented diagnostic and remediation steps.

For each step:
- State what the runbook explicitly says.
- Identify any prerequisites or approval requirements it documents.
- Flag risks to production availability or data integrity.
- Identify details that the runbook does not specify.

Do not invent missing procedures or approval rules. Distinguish documented instructions from your own recommendations, and reference the relevant section or wording where possible.

### Demo 4: Code explanation is not code verification
Tool: GitHub Copilot

Files from the existing demo pack
- `Code/ticket_triage_starter.py`
- `Code/test_ticket_triage.py`

**Prompt:**

Explain how the ticket-triage implementation works.
Refer to these code files:
- Code/ticket_triage_starter.py
- Code/test_ticket_triage.py

Identify:
- The business rules implemented in code.
- Assumptions or edge cases that may be missing.
- Which behaviours can be verified through unit tests.
- Which business rules require clarification rather than inference.

Do not change the files yet. Do not claim that the tests have run.



