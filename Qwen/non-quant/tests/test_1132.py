import pytest
from src_1132 import task_func
import sqlite3
import hashlib
import binascii

def test_task_func():
    # Create an in-memory SQLite database and populate it with test data
    connection = sqlite3.connect(':memory:')
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE users (id INTEGER PRIMARY KEY, password TEXT)''')
    cursor.execute("INSERT INTO users (password) VALUES ('password1')")
    cursor.execute("INSERT INTO users (password) VALUES ('password2')")
    connection.commit()

    # Define a test salt
    test_salt = "testsalt"

    # Call the function under test
    count_updated = task_func(test_salt, cursor)

    # Verify that the correct number of records were updated
    assert count_updated == 2

    # Fetch the updated records to verify the hashed passwords
    cursor.execute("SELECT id, password FROM users")
    updated_users = cursor.fetchall()

    for user in updated_users:
        original_password = user[1].encode('utf-8')
        salted_password = original_password + test_salt.encode('utf-8')
        hash_obj = hashlib.sha256(salted_password)
        expected_hashed_password = binascii.hexlify(hash_obj.digest()).decode('utf-8')
        assert user[1] == expected_hashed_password

    # Close the database connection
    connection.close()