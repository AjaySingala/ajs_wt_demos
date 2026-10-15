# Data Track - MASTER CLASS 2

## Demo 1: Generate a source-to-target transformation
**Tool:**
- Copilot Chat

**Files:**
- customer_portfolio_1200.csv
- Source_Schema.md
- Target_Schema.sql.md

**Prompt:**
You are a senior data engineer. Using the supplied source CSV, source schema and proposed target schema, create a source-to-target mapping specification.

Before writing code, provide a mapping table containing:
- Source column
- Target column and target type
- Transformation or conversion rule
- Data type conversion
- NULL or blank or invalid-value handling
- Validation rule/check
- Whether the rule is fully specified or requires business-owner clarification

Identify fields with no direct source mapping, fields requiring normalization, code fields needing reference validation, and assumptions that must not be silently converted into business rules.

Do not generate the final ETL code yet. 
Do not invent mappings for UNKNOWN segment values. 

Treat distinct customer_id values as distinct unless an approved identity-resolution rule is supplied. 

State the expected target grain and explain how duplicate source rows and multiple versions will be handled in a later step.

Produce the final source-to-target mapping as a Markdown file named source_to_target_mapping.md.

Include the complete column-level mapping, transformation rules, data types, null handling, validation requirements, deduplication considerations, and unresolved business questions.

Use the supplied source and target schemas as the basis. 

Clearly distinguish documented rules from assumptions requiring business approval. Do not invent reference mappings or silently resolve ambiguous business rules.

Make the mapping sufficiently precise for another developer to use it to design the ETL transformation in GitHub Copilot. 

Do not generate the ETL SQL yet.


## DEMO 2: Deduplication and incremental-load design
**Tool:**
- GitHub Copilot

**Prompt:**

Act as a senior data engineer designing an incremental ETL process.

Use the following files in the current VS Code workspace:
- customer_portfolio_1200.csv
- Source_Schema.md
- Target_Schema.sql.md
- source_to_target_mapping.md

Treat the source schema, target schema, and reviewed mapping specification as the design inputs. If they conflict, identify the conflict and ask for clarification rather than silently choosing a rule.

Task 1: Inspect the data and design inputs
1.	Identify exact duplicate source rows.
2.	Identify multiple versions of the same customer_id.
3.	Identify possible same-person records with different customer IDs.
4.	Examine source_updated_at, ingest_batch_id, and source_record_id for their suitability in incremental processing.
5.	Identify missing values and invalid or unresolved reference codes that need exception handling.

Do not assume that matching names or email addresses proves two customer IDs represent the same person.

Task 2: Design the deduplication strategy
Propose deterministic rules for:
- Removing exact duplicate source rows.
- Selecting the winning version for each customer_id.
- Resolving timestamp ties with explicit tie-breakers.
- Routing possible identity matches to an exception queue rather than automatically merging them.

Explain why each rule is appropriate and identify any decision requiring business approval.

Task 3: Design the incremental load
Describe how the ETL will:
- Identify new and changed records.
- Handle late-arriving records and timestamp ties.
- Insert new customers and update existing target records.
- Avoid duplicate inserts or unintended changes when the same batch is processed twice.
- Record rejected rows and unresolved exceptions.
- Reconcile source, processed, rejected, inserted, and updated record counts.

Task 4: Generate the implementation
Generate SQL for the proposed deduplication and incremental-load design.
Before generating the SQL:
- State the SQL dialect and required staging-table assumptions.
- Identify any orchestration parameters or metadata that the implementation requires.
- Explain whether the proposed design uses a target-table MERGE/UPSERT or another mechanism.
- Flag any business rules that remain unresolved.

Keep source data unchanged. 
Do not invent mappings, reference values, or business rules. 
Do not claim that SQL has been executed or tested unless it actually has been.

Deliverables
1.	A concise design explanation.
2.	SQL implementation in customer_portfolio_etl.sql.
3.	Assumptions and open questions.
4.	Reconciliation checks and test cases.
5.	A list of risks that must be resolved before production use.

## DEMO 3: Review the ETL transformation generated in Demo 2

Review the SQL transformation produced in Demo 2 (the customer_portfolio curated incremental-load transformation), using the source CSV, source schema, target schema and mapping specification.

Do a code/design review, not a fresh transformation. Inspect:
- Whether the exact-duplicate partition truly identifies exact duplicates and includes all relevant source columns
- Whether ROW_NUMBER winner selection is deterministic and whether tie-breakers are meaningful
- Whether filtering to the current batch can miss late-arriving data or versions that arrive in a later batch
- Whether the SQL implements a real incremental target MERGE/UPSERT or only selects candidate rows
- Whether existing target rows are inserted/updated idempotently
- Whether NULL, blank, UNKNOWN and invalid reference codes are handled according to documented rules
- Whether possible same-person records with different customer_id values are kept in an exception queue rather than merged
- Whether source-to-target types and date conversions are valid for the stated SQL dialect
- Whether the load has reconciliation counts, rejected-row handling, audit metadata and rollback/restart behaviour

For each finding, cite the relevant SQL fragment, explain the impact, assign High/Medium/Low severity, and propose a correction. 

Separate confirmed code defects from assumptions needing business approval. 

Do not claim the SQL has been run or tested. 

Finish with a prioritized list of tests needed before production use.

Then propose a test suite containing:
1.	Normal valid records
2.	Missing values
3.	Invalid data types or formats
4.	Duplicate candidates
5.	Boundary values
6.	Conflicting records
7.	Late-arriving records, if relevant
8.	Rerun and idempotency checks

For each test, state the input condition, expected behaviour and reason for the test.

Separate defects confirmed from the code from risks that depend on undocumented business rules. 

Do not claim that tests passed unless they were actually executed.
