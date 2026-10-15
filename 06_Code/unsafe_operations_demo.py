import os
import shutil
import sqlite3

# Deliberately unsafe examples for code review only.
# Do not uncomment or execute these operations.

API_TOKEN = "demo-password-12345"  # Hard-coded credential

def clean_application_data(target_dir):
    # RISK 1: Unrestricted recursive deletion
    # shutil.rmtree(target_dir)

    # RISK 2: Excessive privileges and dangerously broad permissions
    # os.system("sudo chmod -R 777 /")

    print(f"Cleanup requested for: {target_dir}")


def get_customer_record(customer_id):
    # RISK 3: SQL injection through string interpolation
    query = (
        "SELECT * FROM customers WHERE customer_id = '"
        + customer_id
        + "'"
    )

    connection = sqlite3.connect("operations.db")
    cursor = connection.cursor()

    try:
        cursor.execute(query)
        return cursor.fetchall()
    finally:
        connection.close()


def remove_old_records():
    connection = sqlite3.connect("operations.db")
    cursor = connection.cursor()

    try:
        # RISK 4: Destructive database operation without safeguards
        # cursor.execute("DROP TABLE customers")

        # RISK 5: Broad deletion without a defined retention condition
        # cursor.execute("DELETE FROM customers")

        connection.commit()
    finally:
        connection.close()


def call_external_service():
    # RISK 6: Credential exposure in logs
    print(f"Using API token: {API_TOKEN}")

    # RISK 7: No timeout, response validation or retry policy
    # response = requests.get("https://example.invalid/api")
    # print(response.text)

    pass
	