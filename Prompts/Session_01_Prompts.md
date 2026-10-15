# SESSION 1 - GENAI & PROMPTING FUNDAMENTALS
## Common to Data and Enterprise Ops

### Demo 1: The same task, five prompt qualities

**Dataset:**
`ops_tickets_200.csv`

**Weak prompt:**
Analyze these tickets and tell me what is important.

**Better:**
Analyze these operational tickets and identify the major patterns.

**Strong:**
You are an operations analyst. Analyze the attached operational tickets and identify the five most significant patterns by customer impact, SLA exposure and recurrence. Quantify each pattern using evidence from the dataset.

**Production-oriented:**
You are a WinTrust operations analyst. Analyze the attached tickets to identify the five most material operational patterns. 

For each pattern provide: 
- evidence, 
- affected customers/services, 
- SLA exposure, 
- business impact, 
- likely contributing factor, 
- recommended next action and confidence. 

Do not invent information. If evidence is insufficient, say so.

### Demo 2: Prompt refinement

**Start with:**
Which tickets should we worry about?

***Refined Prompt:***
You are a WinTrust operations analyst.

Review the supplied operational tickets against the WinTrust SLA policy.

Identify tickets that:
-have breached their SLA
-require escalation
-show evidence of increasing operational risk

For every finding, cite the evidence from the ticket.
Do not infer missing information.

Return:
Ticket ID | Severity | SLA Status | Evidence | Recommendation

### Data-track prompt

Review the operations ticket data from a data-analysis perspective. Identify patterns that could indicate data-quality, reporting, integration or upstream-data issues. Separate genuine data signals from symptoms that may simply reflect application or infrastructure problems.

### Enterprise Ops prompt

Review the operations tickets from an operations-management perspective. Identify tickets that require escalation based on severity, customer criticality, SLA exposure and affected transactions. Return Ticket ID, reason, urgency and recommended next action. Use only evidence from the dataset and SLA policy.
