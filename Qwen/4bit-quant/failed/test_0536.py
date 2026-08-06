import pytest
from src_0536 import task_func
import sqlite3
import os

# Constants
DB_PATH = ":memory:"  # Using in-memory database for testing
TABLE_NAME = "test_table"
NUM_ENTRIES = 10

@pytest.fixture(scope="module")
def setup_db():
    # Setup a test database and table
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    table_creation_sql = (
        "CREATE TABLE IF NOT EXISTS {} (name TEXT, age INTEGER, height INTEGER)".format(
            TABLE_NAME
        )
    )
    cur.execute(table_creation_sql)
    conn.commit()
    conn.close()

@pytest.fixture(scope="module")
def teardown_db():
    # Cleanup after tests
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS {}".format(TABLE_NAME))
    conn.commit()
    conn.close()

def test_task_func_positive_entries(setup_db, teardown_db):
    # Test with positive number of entries
    inserted_rows = task_func(DB_PATH, TABLE_NAME, NUM_ENTRIES)
    assert inserted_rows == NUM_ENTRIES

def test_task_func_zero_entries(setup_db, teardown_db):
    # Test with zero entries
    inserted_rows = task_func(DB_PATH, TABLE_NAME, 0)
    assert inserted_rows == 0

def test_task_func_negative_entries(setup_db, teardown_db):
    # Test with negative number of entries should raise ValueError
    with pytest.raises(ValueError):
        task_func(DB_PATH, TABLE_NAME, -1)

def test_task_func_with_random_seed(setup_db, teardown_db):
    # Test with a specific random seed to ensure reproducibility
    seed_value = 42
    inserted_rows = task_func(DB_PATH, TABLE_NAME, NUM_ENTRIES, random_seed=seed_value)
    assert inserted_rows == NUM_ENTRIES

    # Check the contents of the table to ensure consistency
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT * FROM {}".format(TABLE_NAME))
    rows = cur.fetchall()
    conn.close()

    assert len(rows) == NUM_ENTRIES
    # Add more checks if necessary to verify the data integrity

def test_task_func_with_existing_table(setup_db, teardown_db):
    # Test with an existing table
    # First insert some data to create the table
    task_func(DB_PATH, TABLE_NAME, NUM_ENTRIES)
    
    # Then try inserting more data
    additional_entries = 5
    inserted_rows = task_func(DB_PATH, TABLE_NAME, additional_entries)
    assert inserted_rows == additional_entries

    # Check the total number of rows in the table
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM {}".format(TABLE_NAME))
    count = cur.fetchone()[0]
    conn.close()

    assert count == NUM_ENTRIES + additional_entries