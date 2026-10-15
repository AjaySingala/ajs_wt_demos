# SESSION 3 - DATA-TO-DECISIONS ANALYTICS
## Common foundation, track-specific analysis

Dataset:
`sales_pipeline_300.csv`

### Demo 1A: Explore and analyze the dataset.
Act as a senior business data analyst.

Analyze the supplied file sales_pipeline_300.csv.

STEP 1: INSPECT THE DATA

Identify:
- Available columns and likely data types
- Number of records
- Missing values
- Duplicate records or identifiers
- Inconsistent categories
- Suspicious or invalid values
- Business definitions that cannot be established from
  the file alone

STEP 2: ESTABLISH THE BASELINE

Where the data supports the calculation, determine:
- Total pipeline value
- Average deal value
- Median deal value
- Record counts by deal status
- Closed-won and closed-lost counts
- Win rate, if sufficient information is available

For every metric, state the calculation method and
the relevant population or denominator.

STEP 3: COMPARE BUSINESS DIMENSIONS

Analyze pipeline value and deal outcomes by region,
product, and customer segment where the relevant
fields exist.

Identify:
- Material differences between groups
- Unusual concentrations
- Potential outliers
- Patterns that merit further investigation

For every finding:
- State the metric and evidence
- Provide the relevant sample size
- Explain the business interpretation
- State what the finding does not establish

RULES

Do not invent missing values or business definitions.
Do not treat pipeline value as realized revenue.
Do not infer causation from correlation.
Do not calculate a win rate using an inappropriate
or unexplained denominator.

If a metric cannot be calculated reliably, explain why.

Present the results as a concise analytical report
with an evidence section, findings, limitations,
and questions requiring further investigation.

### Demo 1B: Follow-up prompt.
Select the three findings from your analysis that are
most likely to matter to a business leader.

For each finding, provide:
1. The exact metric
2. The calculation method
3. The relevant population or denominator
4. The business interpretation
5. A possible alternative explanation
6. What additional evidence would be needed

Rank the findings by potential decision relevance,
not merely by the size of the number.

Do not invent findings or business consequences.


### Demo 1C: From observation to insight

Analyze the sales pipeline dataset. Identify three significant patterns across region, product, customer segment, pipeline value, win probability, actual revenue and sales-cycle length. Quantify every claim.

### Demo 1D: Decision-oriented analysis

The leadership team wants to improve pipeline quality rather than simply increase pipeline volume. Identify segments with high pipeline value but weak conversion signals or long sales cycles. Quantify the evidence and recommend where management should investigate further.

### Demo 2: Challenge the analysis
Act as an independent analytics reviewer.

Review the analysis produced from sales_pipeline_300.csv.

Challenge the findings using the following checks.

1. Recheck important totals, averages, percentages,
   and group comparisons.

2. Identify the denominator used for every percentage.
   Determine whether that denominator is appropriate.

3. Check whether pipeline value, expected value,
   closed-won value, and realized revenue have been
   confused.

4. Determine whether a small number of large deals
   could distort averages or group comparisons.

5. Identify missing values, duplicate records,
   inconsistent categories, or suspicious records that
   could affect the findings.

6. Identify conclusions that imply causation when the
   data only demonstrates an association.

7. Identify conclusions that depend on unverified
   business definitions or assumptions.

8. Identify additional data that could materially
   change the interpretation.

For each issue provide:
- Original finding
- Validation check
- Result
- Confidence: High, Medium, or Low
- Limitation
- Required follow-up

Do not claim a calculation has been independently
verified unless you actually recomputed it or provide
a reproducible method.

Clearly distinguish checks you completed from checks
that you could not perform using the supplied data.

Finish with a list of findings that are sufficiently
supported and findings that should not yet be used
for a business decision.

### Demo 3: Create an executive decision brief
Using only the findings from the validated analysis of
sales_pipeline_300.csv, prepare a decision brief for a
sales or business leader.

Include the following sections.

1. EXECUTIVE TAKEAWAY
State the most important supported finding.

2. THREE MATERIAL INSIGHTS
For each insight, provide the supporting metric,
relevant comparison, and business interpretation.

3. TWO POTENTIAL RISKS
Explain the possible business consequence and identify
the evidence supporting the concern.

4. TWO POTENTIAL OPPORTUNITIES
Describe the potential benefit and the additional
evidence needed to validate it.

5. RECOMMENDED NEXT ACTION
Propose a specific and proportionate action based on
the strongest available evidence.

6. FIVE FOLLOW-UP QUESTIONS
Identify questions that should be resolved before
making a significant decision.

7. LIMITATIONS
State what the dataset cannot establish and identify
important assumptions.

RULES

Distinguish observations from interpretations.
Cite the relevant metrics or comparisons.
Disclose important assumptions.
Avoid unsupported causal claims.
Do not invent monetary benefits, forecasts, or
business impacts.
Where the evidence is insufficient, say so.

Maximum length: 500 words.

### Demo 4: Red-team the recommendation
Act as a skeptical executive reviewer.

Challenge the decision brief you just produced.

Identify:

1. Claims that may be overstated
2. Conclusions that depend on assumptions
3. Evidence that is weak or incomplete
4. Risks that may have been overlooked
5. Missing information that could change the decision
6. Statements that sound more certain than the evidence
   supports
7. Recommendations that are not sufficiently justified

For each issue provide:
- Original statement
- Why it is questionable
- Evidence that is missing
- A safer replacement statement

Do not rewrite the entire brief.

Do not introduce new facts. Preserve the distinction
between evidence, interpretation, and uncertainty.


### Demo 5:Data team application: Data-quality analysis: Data-track prompt: 

**Simple Prompt:**

Analyze the dataset as a data analyst. Identify possible data-quality issues, inconsistent values, suspicious records, outliers and metrics that could be misleading. Distinguish data-quality findings from genuine business findings.

**Improved Prompt:**

Act as a senior data analyst investigating the supplied
WinTrust data-quality exceptions dataset.

Identify the most material data-quality patterns.

For each finding provide:

- Data-quality dimension
- Number of affected records
- Relevant denominator and error rate
- Supporting evidence
- Potential downstream impact
- Possible explanation, clearly labeled as a hypothesis
- Validation required
- Recommended next step

Rank the findings by business significance, not merely
by frequency.

Do not infer a root cause from a symptom alone.
Do not claim that a data defect caused a business
outcome unless the supplied evidence establishes
that relationship.

Identify missing information that would materially
change the investigation.


### Demo 6: Enterprise Operations application: Ticket and SLA analysis: Enterprise Ops prompt

**Simple Prompt:**

Analyze the dataset from an operational-management perspective. Identify patterns that could indicate process bottlenecks, slow sales cycles, regional execution issues or customer-risk concentration. Recommend three operational investigations.

**Improved Prompt:**

Act as an Enterprise Operations analyst.

Analyze the supplied WinTrust operational ticket dataset.

Where the relevant fields are available, summarize:

- Ticket volumes by severity and category
- SLA-breach counts and rates
- Differences between ticket groups
- Recurring symptoms
- Potential concentration of operational risk
- Records requiring further investigation

For each finding, provide the calculation method,
numerator, denominator, and relevant limitations.

Separate:
1. Observed facts
2. Potential explanations
3. Recommended investigations

Do not assume that a high ticket count proves a root
cause.

Do not recommend closing, suppressing, or downgrading
incidents based only on statistical patterns.

Identify any missing definitions or fields that prevent
a reliable conclusion.


### Demo 7A: GitHub Copilot example: Data team
Use:
`sales_pipeline_300.csv`

Act as a senior data analyst and SQL developer.

The WinTrust data team needs a sales performance summary.

The source file is sales_pipeline_300.csv, with these columns:
Deal_ID, Month, Region, Product, Customer_Segment,
Pipeline_Value_INR, Win_Probability, Actual_Revenue_INR,
Sales_Cycle_Days, Customer_Risk

Generate SQL for a table named sales_pipeline with the same columns.

The query must:
1.	Summarize pipeline value and actual revenue by Month, Region and Product.
2.	Calculate the average Win_Probability and average Sales_Cycle_Days.
3.	Count the number of records in each group.
4.	Handle NULL values appropriately and explain the chosen approach.
5.	Use clear aliases for the aggregated columns.

Constraints:
- Do not invent columns such as Deal_Status.
- Do not treat pipeline value as actual revenue.
- Do not assume the representation of Win_Probability without stating the assumption.
- Do not infer closed-won or closed-lost counts.
- Do not invent business rules or filters.

Provide the SQL, explain each aggregation, identify assumptions,
and suggest test cases to validate the results.

State which SQL dialect you have assumed.
Do not claim the query has been executed or validated unless it has.

### Demo 7B: GitHub Copilot example: Data team: SQL Challenge
Review the SQL query you generated.

Check for:
- Incorrect aggregation or grouping
- NULL handling
- Duplicate records affecting totals
- Incorrect interpretation of Win_Probability
- Confusion between Pipeline_Value_INR and Actual_Revenue_INR
- Unsupported assumptions or invented business rules

For each issue, explain the risk and propose a correction.
Then provide test cases that would reveal the issue.

Do not claim the query is correct merely because it is syntactically valid.


### Python Script Generation for Data Team (if required).
I need a reusable Python 3.13 script for profiling a
CSV dataset.

The script must report:

1. Row and column counts
2. Column names and inferred data types
3. Missing-value counts and percentages
4. Duplicate-row counts
5. Duplicate identifier counts when an identifier
   column is specified
6. Distinct-value counts for categorical columns
7. Minimum, maximum, mean, and median for applicable
   numeric columns
8. Invalid or unexpected values when validation rules
   are supplied

Requirements:

- Use pandas.
- Accept the input CSV path as a command-line argument.
- Do not modify the source file.
- Handle empty files and missing columns safely.
- Make the output readable and suitable for review.
- Do not silently discard invalid records.
- Clearly distinguish automatically inferred properties
  from business validation rules.

Generate tests covering normal input, missing values,
duplicate identifiers, an empty file, and malformed
input.

Explain the implementation and identify limitations
before considering the code complete.

### Demo 8: GitHub Copilot example: Enterprise Operations

Create a Python 3.13 script that reads an operational
ticket CSV and calculates ticket volumes and SLA
performance.

Requirements:

1. Accept the CSV path as a command-line argument.
2. Validate that required columns exist.
3. Summarize ticket counts by severity and category.
4. Calculate SLA-breach counts and rates where the
   available fields support the calculation.
5. Clearly define the denominator for each rate.
6. Handle missing SLA values explicitly.
7. Do not treat missing SLA values as successful
   outcomes.
8. Report invalid or inconsistent records separately.
9. Do not modify the input file.
10. Produce a readable summary suitable for review.

Generate tests for:
- A normal ticket
- A ticket exactly at the SLA boundary
- A breached ticket
- A missing SLA value
- An invalid severity
- An empty dataset

Explain the business rules and calculation logic.

Do not invent SLA definitions. If a definition is
missing, identify it as a requirement to resolve.

Provide the code, tests, and execution instructions.

### Reusable analytical prompt template
Act as a [business/data/operations] analyst.

BUSINESS QUESTION
[State the business problem or decision.]

DATASET
[Identify the file, relevant fields, reporting period,
and available business definitions.]

ANALYSIS

1. Inspect the data and its definitions.
2. Establish baseline metrics.
3. Compare relevant groups.
4. Identify meaningful patterns and anomalies.
5. Distinguish observations, hypotheses, and
   recommendations.
6. Identify limitations and missing information.

FOR EACH IMPORTANT FINDING, PROVIDE

- Metric and calculation method
- Numerator and denominator where relevant
- Supporting evidence
- Business interpretation
- Confidence and limitations
- Follow-up validation

CONSTRAINTS

- Do not invent missing information.
- Do not infer causation from correlation.
- Do not confuse potential value with realized outcomes.
- State when the data cannot answer the question.

OUTPUT

Produce an evidence-based report with prioritized
insights, risks, opportunities, and recommended
next steps.

Before finalizing, challenge the calculations and
identify conclusions that may be overstated.

### Hands-on Lab Exercise:
**Input**
sales_pipeline_300.csv

**Tools:**
- Microsoft Copilot Chat is the primary tool.
- GitHub Copilot may be used if you want to validate or reproduce calculations with code.

**Task:**
- Inspect the dataset and establish baseline metrics.
- Analyze relevant differences across regions, products, customer segments, and deal outcomes.
- Identify three meaningful insights.
- Identify two potential risks.
- Identify two potential opportunities.
- Challenge at least two findings.
- Prepare one executive recommendation.
- Identify five follow-up questions.

**Deliverable:**
Evidence table + recommendation summary.

#### Hands-on prompt (do not share): 
Act as a senior business data analyst supporting a
WinTrust business leader.

Analyze sales_pipeline_300.csv to determine where
management attention may be required.

FIRST: INSPECT THE DATA

Identify the columns, data types, missing values,
duplicate identifiers, and relevant business
definitions.

Then:

1. Establish baseline pipeline metrics.

2. Compare regions, products, customer segments, and
   deal outcomes wherever the data supports the
   comparison.

3. Identify three material insights, two potential
   risks, and two potential opportunities.

4. For each finding, provide the supporting metric,
   calculation method, relevant sample size, and
   business interpretation.

5. Identify five questions that management should
   resolve before making a significant decision.

6. Produce one executive recommendation based on the
   strongest supported evidence.

VALIDATION REQUIREMENTS

- Check the denominator for every percentage.
- Distinguish open pipeline from closed-won business
  and realized revenue.
- Do not infer causation from correlation.
- Identify whether averages could be distorted by
  large deals or outliers.
- Separate observations from hypotheses.
- State what cannot be established from the data.
- Do not invent financial benefits or explanations.

OUTPUT

Produce a concise decision brief containing:

- Executive takeaway
- Three insights
- Two risks
- Two opportunities
- Five follow-up questions
- One recommendation
- Limitations

Before finalizing, challenge your own findings and
revise any conclusion that is not adequately supported.


### Additional GitHub Copilot demo

Give GitHub Copilot a Python function that calculates weighted pipeline.
Use:
    - weighted_pipeline.py

*Prompt:*
Review this calculation for correctness. Identify edge cases such as null probabilities, percentages stored as decimals, negative values and missing revenue. Add unit tests.

---
*A very detailed alternate prompt:*

Review this Python calculation for correctness and reliability. Do not modify the code yet.

Analyze the calculate_weighted_pipeline() function and identify potential problems or ambiguous assumptions.

Specifically check for these edge cases:
- None or missing probability
- probability represented as a decimal, such as 0.25
- probability represented as a percentage, such as 25
- probability values below 0 or above 1
- missing revenue
- None revenue
- negative revenue
- zero revenue
- empty input
- invalid data types
- unexpected or malformed opportunity records

For each issue:
1. Explain what could go wrong.
2. Give a concrete example.
3. State whether the current function handles it correctly.
4. Recommend the expected business rule.
Do not assume that the correct business rule is obvious. Clearly distinguish between a technical problem and a business-rule decision.
After the review, generate a comprehensive set of unit tests that would expose the identified issues. Do not fix the implementation yet.

---
*After participants have reviewed the output:*

Based on the issues identified above, propose a corrected implementation of calculate_weighted_pipeline().
Before providing the code, state the assumptions and business rules you are implementing.
Then provide the revised function and explain how each identified edge case is handled.
Finally, provide the unit tests that should pass against the revised implementation.
---
