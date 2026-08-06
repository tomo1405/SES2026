import pytest
from src_0843 import task_func
import os
import sqlite3

def test_task_func():
    # Define test parameters
    db_path = 'test_db.sqlite'
    num_entries = 5
    random_seed = 42

    # Call the function under test
    result = task_func(db_path, num_entries, random_seed=random_seed)

    # Check if the result is the correct path
    assert result == db_path

    # Check if the database file exists
    assert os.path.exists(db_path)

    # Connect to the database and check its contents
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    # Check if the table exists
    c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users'")
    assert c.fetchone() == ('users',)

    # Check the number of entries
    c.execute("SELECT COUNT(*) FROM users")
    assert c.fetchone()[0] == num_entries

    # Check the data integrity
    c.execute("SELECT name, age, country FROM users")
    rows = c.fetchall()
    for row in rows:
        assert row[0] in ['Alice', 'Bob', 'Charlie', 'Dave', 'Eve']
        assert 20 <= row[1] <= 60
        assert row[2] in ['USA', 'UK', 'Canada', 'Australia', 'India']

    # Clean up
    conn.close()
    os.remove(db_path)