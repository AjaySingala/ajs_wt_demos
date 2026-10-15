# MASTER CLASS IV - GENAI IN AGENTS
## Common to Data + Enterprise Ops
## No agent is created or used

## Demo 1: From Copilot response to agentic decision-making
**Incident details:**

INC-5837: Payment Processing Degradation
Root cause unconfirmed
Environment: Simulated production | Duration: 22 minutes and ongoing

Business impact
- Payment API success rate dropped from 99.95% to 96.8%.
- Payment response latency increased from 350 ms to 2.4 seconds at p95.
- 1,240 requests were retried during the incident window.
- The number of duplicate charges, if any, has not been established.

Observed technical signals
- Database CPU peaked at 94%; connection-pool utilization reached 97%.
- Queue depth increased from 800 to 12,600 messages.
- A payment reconciliation batch started 6 minutes before the first alert.
- A new API release was deployed 18 minutes before the first alert.
- An upstream payment-provider timeout rate increased from 0.2% to 4.5%.
- Application logs show intermittent timeout and retry messages.

Evidence gaps
- No distributed trace linking a failed payment to its downstream dependencies.
- No query-plan or database wait analysis.
- No confirmed comparison between the new release and the previous version.
- No queue message age or dead-letter analysis.
- No reconciliation result confirming whether payments were duplicated, delayed, or lost.
- No approved rollback decision or confirmation that rollback would be safe.

Constraints
- Do not retry or replay payments without idempotency and reconciliation checks.
- Do not restart services or roll back the release without the authorized incident process.
- Do not assume the batch job or new release caused the incident merely because of timing.
- Preserve relevant diagnostic and audit evidence.

**Prompt 1: Summarize:**
Summarize incident INC-5837 for an incident commander.

Organize the summary into:
- Confirmed observations
- Business impact
- Plausible hypotheses
- Critical unknowns
- Immediate risks requiring attention

Do not declare a root cause. Do not recommend executing a production change. Use only the supplied incident information.

**Prompt 2: Recommend:**
Based only on the incident information, recommend the three highest-priority next steps for the incident commander.

For each step, state:
- Why it matters
- What evidence it should obtain
- Whether it is read-only or changes system state
- What decision it would help the incident commander make

Prioritize customer and payment integrity, evidence gathering, and service stability. Do not invent available tools, operational procedures, or approval authority. Do not present a hypothesis as a confirmed cause.


**Prompt 3: verify before acting:**
For each recommended step, identify the information and checks required before anyone acts on its results.

Distinguish:
1.	Information that can be collected using read-only diagnostics.
2.	Evidence needed to confirm or reject each major hypothesis.
3.	Actions that could affect payment integrity, service availability, or customer outcomes.
4.	Actions requiring explicit human approval.
5.	Conditions under which the team should stop and escalate rather than proceed.

Do not invent WinTrust procedures, thresholds, or authorization roles.

**Prompt 4: introduce dynamic action selection:**
_Possible findings and Adaptive reasoning_

**Prompt:**
Consider a hypothetical incident-investigation system for INC-5837. Do not build or invoke an agent.

Explain how its next diagnostic step might change depending on these possible findings:
- Finding A: Errors occur mainly on the new application release.
- Finding B: Errors correlate with upstream payment-provider timeouts.
- Finding C: Queue depth continues rising while consumers are healthy.
- Finding D: Payment reconciliation reveals possible duplicate or unresolved transactions.

For each finding, identify:
- The next investigation direction
- The evidence still required
- Any actions that must remain human-controlled
- A condition for stopping or escalating

Do not assume any of these findings has actually been observed. Do not prescribe production changes without sufficient evidence and authorization.

## Demo 2: Deterministic workflow versus agentic behaviour
- Use: `incident_review_workflow.py`
- Open in VS Code
- Tool GitHub copilot

**Prompt:**
Review incident_review_workflow.py.

Do not build an agent or add external integrations.

Explain:
1.	Which operations are deterministic and why.
2.	Which decisions are currently fixed regardless of intermediate findings.
3.	Where a real investigation might need to select its next step based on newly obtained evidence.
4.	Which decisions could reasonably use GenAI assistance and what evidence would be needed.
5.	Which actions must remain subject to human approval.
6.	What controls would be needed before this workflow could safely become more adaptive.

Propose a comparison between the current deterministic workflow and a hypothetical agentic design. Discuss complexity, auditability, testing, operational risk, and business value.

Do not invent approved operational thresholds. Do not claim to have run or tested the script. Do not implement the agentic design.
