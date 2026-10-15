# Source schema: customer_portfolio_1200.csv

The CSV is a synthetic customer portfolio extract for Session 11 demos. It contains 1,240+ rows because the nominal 1,200 customer records are supplemented with deliberate duplicate/version scenarios for teaching. Do not assume one row equals one unique customer.

| Column | Suggested source type | Meaning / handling |
|---|---|---|
| source_record_id | VARCHAR | Unique identifier for a source row in normal source data; exact duplicate examples repeat it. |
| source_system | VARCHAR | Originating system label. |
| ingest_batch_id | VARCHAR | Batch identifier, including a later batch for changed records. |
| source_updated_at | TIMESTAMP | Source-side update time. Use as a candidate incremental watermark only after considering late-arriving records and tie-breaking. |
| customer_id | VARCHAR | Customer identifier as supplied by source. Do not merge distinct IDs solely because names/emails match. |
| full_name | VARCHAR | Customer name, with some whitespace variation. |
| email | VARCHAR | Email, with blanks and case variation. |
| phone | VARCHAR | Phone, with blanks and formatting variation. |
| date_of_birth | DATE | Birth date as supplied. Treat as sensitive; only use when required for the exercise. |
| address_line_1 | VARCHAR | Address line. |
| city | VARCHAR | City. |
| state_code | VARCHAR | State code, with some blanks. |
| postal_code | VARCHAR | Postal code; preserve as text to retain leading zeros. |
| segment_code | VARCHAR | Customer segment code; includes UNKNOWN values requiring rule clarification. |
| status_code | VARCHAR | Customer status code. |
| annual_income_inr | DECIMAL(18,2) | Annual income in INR; includes missing values. |
| relationship_manager_id | VARCHAR | Assigned relationship manager. |
| record_effective_from | DATE | Effective-from date. |
| record_effective_to | DATE / NULL | Effective-to date; blank means not supplied, not automatically a guaranteed current record. |
| is_current_record | CHAR(1) | Source current-record indicator, not independently verified. |

Important: all rows and values are synthetic. The dataset is designed for SQL/ETL demonstrations, not for real customer decisions. The nominal filename indicates the intended portfolio size; appended rows intentionally demonstrate exact duplicates, later versions and possible-match records.
