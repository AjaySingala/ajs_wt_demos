# Source-to-Target Mapping Specification: customer_portfolio_curated

## 1. Document Overview & Purpose
This document provides a precise, developer-ready source-to-target mapping (STM) specification for loading the `customer_portfolio_curated` target analytical dimension from the `customer_portfolio_1200.csv` source extract. 

This specification is structured for implementation via an ETL pipeline (to be built using tools like GitHub Copilot). It strictly enforces data governance rules: no ambiguous business rules are silently resolved, reference codes with `UNKNOWN` values remain unmapped pending business sign-off, and distinct `customer_id` values are maintained separately unless explicit identity resolution rules are provided.

---

## 2. Target Grain & Deduplication / Versioning Strategy

### 2.1 Target Grain
* **Grain Definition:** One row per unique business key `customer_id`.
* **Constraint Enforcement:** Enforced by the primary key constraint on `customer_id` in the `customer_portfolio_curated` table.

### 2.2 Source Characteristics & Deduplication Handling
* **Source Dataset Profile:** The source extract (`customer_portfolio_1200.csv`) contains 1,240+ rows representing nominal 1,200 customer records supplemented with exact duplicates (`source_record_id` repeats) and later versions across ingestion batches (`ingest_batch_id`, `source_updated_at`).
* **Deduplication & Pre-processing Rule:** 
  1. Because the target primary key prevents multiple current target rows for a single `customer_id`, the ETL pipeline must implement a windowing or ranking function prior to final insertion.
  2. **Ranking Logic:** Order source rows partition by `customer_id` ordered by `source_updated_at DESC`, `ingest_batch_id DESC`. 
  3. **Identity Resolution:** Do **not** merge distinct `customer_id` values even if names or emails match, unless an approved enterprise identity resolution rule is explicitly provided.

---

## 3. Column-Level Mapping Specification

| Target Column | Target Data Type | Source Column(s) | Transformation / Conversion Rule | Null / Blank Handling | Validation Rule | Clarification Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **`customer_id`** | `VARCHAR(20)` | `customer_id` | Direct copy from source. Maintain as primary business key. | Reject nulls or blanks (violates PK constraint). | Check for non-null, correct format, uniqueness across target. | Fully Specified |
| **`customer_name`** | `VARCHAR(200)` | `full_name` | Trim leading/trailing whitespace (`TRIM(full_name)`). | Retain NULL if source is blank or missing. | Max length $\le$ 200 characters. | Fully Specified |
| **`email_normalized`** | `VARCHAR(320)` | `email` | Trim whitespace and lowercase (`LOWER(TRIM(email))`). | Blank or missing values become NULL. Do not invent/synthesize an email. | Valid email structure containing `@` symbol. | Fully Specified |
| **`phone_normalized`** | `VARCHAR(20)` | `phone` | Trim whitespace; preserve digits and leading country code if present. Do not infer missing digits. | Blank or missing values become NULL. | Only digits and optional leading `+`; length $\le$ 20. | Fully Specified |
| **`date_of_birth`** | `DATE` | `date_of_birth` | Direct date casting/parsing. Handle as sensitive data. | Retain NULL if missing. | Must be a valid past date; age reasonableness check (e.g., age 0 to 120). | Fully Specified |
| **`address_line_1`** | `VARCHAR(250)` | `address_line_1` | Trim whitespace (`TRIM(address_line_1)`). | Retain NULL or blank as-is. | Max length $\le$ 250 characters. | Fully Specified |
| **`city`** | `VARCHAR(100)` | `city` | Trim whitespace and normalize capitalization if applicable. | Retain NULL if missing. | Max length $\le$ 100 characters. | Fully Specified |
| **`state_code`** | `CHAR(2)` | `state_code` | Trim whitespace. Source includes some blank entries. | Blank values become NULL. | Must match approved state code reference list. | **Requires Clarification** (Handling of unlisted/blank state codes) |
| **`postal_code`** | `VARCHAR(12)` | `postal_code` | Cast/preserve strictly as text (`VARCHAR`) to retain leading zeros. | Retain as-is or NULL if missing. | Match expected postal code pattern (e.g., 6 digits for Indian PIN codes). | Fully Specified |
| **`segment`** | `VARCHAR(20)` | `segment_code` | Direct mapping from `segment_code`. Do **not** map `UNKNOWN` to a default segment value. | Retain `UNKNOWN` or NULL as supplied; do not silently substitute. | Must exist in approved segment reference table. | **Requires Clarification** (`UNKNOWN` handling policy) |
| **`customer_status`** | `VARCHAR(20)` | `status_code` | Direct mapping from `status_code` using approved reference mapping. | Retain NULL if missing. | Must match valid status reference values. | **Requires Clarification** (Permitted status values list) |
| **`annual_income_inr`** | `DECIMAL(18,2)` | `annual_income_inr` | Direct numeric cast. Includes missing values in source. | Missing values become NULL. | Must be $\ge$ 0 (non-negative income). | Fully Specified |
| **`relationship_manager_id`** | `VARCHAR(20)` | `relationship_manager_id` | Direct copy. | Retain NULL if unassigned. | Validate against active RM roster if available. | **Requires Clarification** (Handling of inactive/unassigned RMs) |
| **`source_system`** | `VARCHAR(30)` | `source_system` | Direct copy of originating system label. | Cannot be null. | Must be a recognized source system identifier string. | Fully Specified |
| **`source_updated_at`** | `TIMESTAMP` | `source_updated_at` | Direct timestamp copy. Candidate incremental watermark (evaluate late-arriving records separately). | Cannot be null. | Valid timestamp format. | Fully Specified |
| **`record_effective_from`** | `DATE` | `record_effective_from` | Direct date copy. | Cannot be null. | Valid date format; must be $\le$ current date. | Fully Specified |
| **`record_effective_to`** | `DATE` | `record_effective_to` | Blank means not supplied, not automatically a guaranteed current record. Blank source values represented as NULL. | Blank/missing values converted to NULL. | If populated, must be $\ge$ `record_effective_from`. | **Requires Clarification** (Open-ended date business meaning) |
| **`is_current_record`** | `BOOLEAN` | `is_current_record` | Convert source CHAR(1) ('Y'/'N') to target BOOLEAN (`TRUE`/`FALSE`). | Default to FALSE or NULL if blank. | Must evaluate strictly to boolean TRUE or FALSE. | **Requires Clarification** (Independent verification of source flag) |
| **`source_record_id`** | `VARCHAR(20)` | `source_record_id` | Direct copy of unique source row identifier (note: exact duplicate examples repeat it). | Cannot be null. | Unique per source batch/system extract. | Fully Specified |
| **`ingest_batch_id`** | `VARCHAR(20)` | `ingest_batch_id` | Direct copy of batch identifier, including later batches for changed records. | Cannot be null. | Valid batch tracking identifier format. | Fully Specified |
| **`load_timestamp`** | `TIMESTAMP` | *None* (ETL Runtime) | Assigned dynamically by the ETL runtime at the time of table load (`CURRENT_TIMESTAMP`). | Populated automatically by ETL engine. | Must be $\ge$ extraction timestamp. | Fully Specified |

---

## 4. Summary of Assumptions & Unresolved Business Questions

1. **Segment & Status Reference Integrity:** The source dataset includes `UNKNOWN` segment values and codes. Per project guidelines, these must **not** be silently mapped to default operational values. Business owners must provide the target handling policy for unmapped codes.
2. **Identity Resolution:** Distinct `customer_id` values must remain separate. Any future entity consolidation across matching names/emails requires explicit data stewardship approval and is excluded from this pipeline release.
3. **Current Record Flags & Effective Dates:** Source-supplied flags (`is_current_record`) and open-ended effective dates (`record_effective_to` as NULL) are accepted as-is from the source extract but require formal validation with data governance owners to ensure SCD Type 2 logic aligns correctly downstream.