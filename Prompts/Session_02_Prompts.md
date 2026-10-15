# SESSION 2 - GENAI FOR RESEARCH, SYNTHESIS & EXECUTIVE COMMUNICATION
## Common to Data and Enterprise Ops

Documents:
- `WinTrust_CEO_Strategy_Briefing_Source.docx`
- `WinTrust_Malicious_Operations_Note.docx`

### Demo 1A: Improved Research Prompt
Act as an enterprise AI risk analyst.

Using only the documents:
1. WinTrust_GenAI_Security_Guidelines.docx
2. WinTrust_Malicious_Operations_Note.docx

identify the security risks and control considerations relevant to employees using Generative AI.

For each item provide:

1. Risk
2. Evidence from the source documents
3. Source document
4. Why the risk matters
5. Recommended control
6. Classification: Fact, Inference, Recommendation, or Unknown

Rules:
- Do not use external knowledge.
- Do not invent policies or controls that are not supported by the documents.
- If the documents do not provide enough information, say "Not specified in the source material."
- Clearly distinguish source evidence from your interpretation.

End with a section titled "Information Missing from the Sources".

### Demo 1B: The Unsupported Claim Test
Based on the same documents, determine whether WinTrust should allocate $5 million to a Generative AI security program in 2026.

Provide:
- evidence supporting the investment
- evidence against the investment
- assumptions required
- missing information
- recommendation


### Demo 2: Multi-Document Executive Synthesis

Documents:
- `WinTrust_CEO_Strategy_Briefing_Source.docx`
- `WinTrust_GenAI_Security_Guidelines.docx`
- `WinTrust_Malicious_Operations_Note.docx`

**Prompt:**
Analyze the three supplied WinTrust documents together.

Create a cross-document synthesis with these sections:

1. Strategic priorities
2. Opportunities
3. Risks
4. Constraints
5. Areas of agreement
6. Areas of tension or conflict
7. Important assumptions
8. Missing information
9. Questions that leadership should resolve

For every material point:
- identify the source document
- distinguish Fact from Inference
- do not merge separate statements into a single fact.

Do not recommend a course of action until the evidence has been synthesized.

### Demo 3: Challenge the briefing (Find the Contradictions)

Review all supplied documents as a critical analyst.

Identify statements that:

1. directly contradict each other
2. appear inconsistent
3. use different definitions for the same concept
4. describe different priorities
5. contain assumptions that may conflict

For each potential conflict provide:

- Source A
- Source A position
- Source B
- Source B position
- Nature of the conflict
- Whether the conflict is explicit or inferred
- Why it matters
- What question a human should resolve

Do not attempt to resolve the conflict yourself unless the documents provide enough evidence.

### Demo 4: Find What Is Missing

Review the supplied documents as if you were preparing a briefing for senior leadership.

Identify the information that is missing but could materially change the analysis.

Create a table with:

| Missing information | Why it matters | Decision affected | How to obtain it |

Prioritize the missing information as:
- Critical
- Important
- Useful

Do not invent the missing information.


### Data-track prompt

Rewrite the briefing for a Chief Data Officer. Emphasize data quality, data ownership, analytical reliability, data-product opportunities and controls. Do not introduce technical recommendations unless they affect a business decision.

### Enterprise Ops prompt

Rewrite the briefing for a COO. Emphasize operational resilience, incident management, productivity opportunities, runbook opportunities, operational risk and human-control requirements.

### GitHub Copilot demo

Open a small Markdown briefing file (Documents/WinTrust_Executive_Briefing_Draft.md) and ask GitHub Copilot:

**Prompt:**
Review this executive briefing for unsupported claims, ambiguous wording, repetition and missing evidence. Suggest edits but preserve the author's intent.

### Demo 5: Executive Briefing Transformation

Take the research output (_from Demo 1A_) and use this prompt:

**Prompt:**

Convert the validated analysis into a one-page CEO briefing.

Audience:
WinTrust CEO

The briefing must contain:

1. Executive takeaway
2. What has changed
3. Three material opportunities
4. Three material risks
5. Important evidence
6. What remains uncertain
7. Decisions or questions requiring leadership attention

Rules:
- Use decision-oriented language.
- Avoid operational detail unless it affects a leadership decision.
- Separate evidence from interpretation.
- Do not introduce new facts.
- Preserve important uncertainty.
- Do not make recommendations that are unsupported by the source material.

Maximum length: 500 words.

