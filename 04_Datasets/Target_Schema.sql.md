# Target schema: customer_portfolio_curated

This is the target model to use in Demo 1. It is a proposed analytical customer dimension, not an existing production schema.

```sql
CREATE TABLE customer_portfolio_curated (
    customer_id              VARCHAR(20) PRIMARY KEY,
    customer_name            VARCHAR(200),
    email_normalized         VARCHAR(320),
    phone_normalized         VARCHAR(20),
    date_of_birth            DATE,
    address_line_1           VARCHAR(250),
    city                     VARCHAR(100),
    state_code               CHAR(2),
    postal_code              VARCHAR(12),
    segment                  VARCHAR(20),
    customer_status          VARCHAR(20),
    annual_income_inr        DECIMAL(18,2),
    relationship_manager_id  VARCHAR(20),
    source_system            VARCHAR(30),
    source_updated_at        TIMESTAMP,
    record_effective_from    DATE,
    record_effective_to      DATE,
    is_current_record        BOOLEAN,
    source_record_id         VARCHAR(20),
    ingest_batch_id          VARCHAR(20),
    load_timestamp           TIMESTAMP
);
```

Mapping principles for the demo:
- `customer_id` is the business key for this exercise. Do not merge different IDs automatically.
- `customer_name` is trimmed `full_name`.
- `email_normalized` is trimmed lowercase email; blank becomes NULL, but do not invent an email.
- `phone_normalized` requires an agreed normalization rule. For this demo, trim whitespace and preserve digits plus a leading country code if present; do not infer missing digits.
- `segment` and `customer_status` require approved reference mappings. Do not map `UNKNOWN` to a default segment.
- `postal_code` stays text.
- `is_current_record` conversion from Y/N to boolean is straightforward, but the meaning must be verified with the source owner.
- `load_timestamp` is assigned by the ETL runtime, not copied from source.
- Source values and business assumptions must be documented. `record_effective_to` blank should be represented as NULL.
- The target primary key prevents multiple current target rows for one `customer_id`; it does not by itself decide which source version wins.
