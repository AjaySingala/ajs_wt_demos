# Data Track - MASTER CLASS 1

## Vague prompt:
Use:
- `sales_pipeline_300.csv` 

**Prompt:**
Look at the sales pipeline data and generate a SQL query to show sales performance by month, region and product.

## Demo 1: Generate a pipeline analysis query
Use:
- `sales_pipeline_300.csv` 

Columns:
`Deal_ID, Month, Region, Product, Customer_Segment, Pipeline_Value_INR, Win_Probability, Actual_Revenue_INR, Sales_Cycle_Days, Customer_Risk`

### Task: generate a query that reports monthly performance by region and product.

**Prompt:**
Generate a SQL query for monthly sales-pipeline analysis using the supplied schema.

Return one row per Month, Region and Product, with:
- Number of records
- Total Pipeline_Value_INR
- Total Actual_Revenue_INR
- Average Win_Probability
- Average Sales_Cycle_Days

Requirements:
- Use the exact column names supplied.
- Do not introduce Deal_Status or classify deals as won or lost.
- Do not treat pipeline value as actual revenue.
- Explain whether Win_Probability should be stored as a fraction or percentage and how that affects interpretation. Do not convert it without confirming the representation.
- Explain how NULL values affect each aggregate.
- State the SQL dialect and identify any syntax that may need adjustment for another dialect.
- Provide validation queries for record counts and aggregate totals.
- Do not claim execution or validation unless it has actually been performed.

## Demo 2: Advanced SQL, window functions and join safety

### Exercise: identify the highest-value pipeline record in each region, including ties.

*Prompt:**
Using the supplied sales-pipeline schema, write a SQL query that returns the highest Pipeline_Value_INR record or records within each Region.

Requirements:
- Use a window function.
- Preserve ties rather than arbitrarily selecting one record.
- Define how NULL pipeline values should be handled.
- Include Deal_ID, Region, Product, Month and Pipeline_Value_INR.
- Explain the difference between ROW_NUMBER, RANK and DENSE_RANK for this requirement.
- State the SQL dialect.
- Provide a small synthetic example with tied values and show the expected ranking.
- Do not invent a business rule for resolving ties.

## Demo 3: Turn data-quality requirements into SQL
Use:
- `data_quality_exceptions_120.csv` or `data_quality_incidents_24.csv`

### Demonstrate three types of queries:
- Detection: find candidate records that violate a stated rule.
- Measurement: count and categorize exceptions.
- Verification: compare records before and after a proposed correction, without changing source data.

**Prompt:**
Act as a senior data-quality engineer.

Inspect the supplied data-quality dataset and its accompanying standards. First list the actual columns and identify the documented quality rules.

For each rule that can be expressed in SQL, perform the following three activities:
A. Detection
- Generate a read-only SQL query that identifies records violating the documented rule.
- Return the record identifier, relevant field values and a clear exception reason.
- Distinguish confirmed rule violations from suspicious records that require investigation.

B. Measurement
- Generate a summary query that counts exceptions by rule.
- Where useful, show counts by relevant category and calculate the percentage of affected records using a clearly defined denominator.
- Ensure the counting method does not unintentionally double-count records.

C. Verification of a proposed correction
- Where the supplied standards support a correction, express the proposed transformation as a read-only SQL expression or query.
- Compare original and proposed values.
- Generate checks to determine whether the proposed output satisfies the documented rule.
- Check for unresolved exceptions, unexpected changes and input/output record-count differences.
- Explain what evidence is required before the correction can be approved.

Do not invent acceptable values, reference mappings, uniqueness rules or remediation policies. If the available information is insufficient, identify the unresolved question instead of guessing.

Do not update, delete or repair source records. Do not claim that any query has been executed or that any correction has been verified unless the relevant checks have actually been performed.



