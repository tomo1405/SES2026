import pytest
from src_0993 import task_func
import sqlite3
import os

@pytest.fixture(scope="module")
def setup_database():
    # Create a temporary database file
    db_path = "test_database.db"
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS paths (path TEXT UNIQUE)")
    conn.commit()
    conn.close()
    yield db_path
    # Clean up the temporary database file
    os.remove(db_path)

def test_task_func_default_values(setup_database):
    path_to_append = "path/to/whatever"
    database = setup_database
    result = task_func(path_to_append=path_to_append, database=database)
    assert result == path_to_append

    # Check if the path is inserted into the database
    conn = sqlite3.connect(database)
    cur = conn.cursor()
    cur.execute("SELECT * FROM paths WHERE path=?", (path_to_append,))
    row = cur.fetchone()
    conn.close()
    assert row is not None and row[0] == path_to_append

def test_task_func_custom_values(setup_database):
    custom_path = "custom/path"
    database = setup_database
    result = task_func(path_to_append=custom_path, database=database)
    assert result == custom_path

    # Check if the custom path is inserted into the database
    conn = sqlite3.connect(database)
    cur = conn.cursor()
    cur.execute("SELECT * FROM paths WHERE path=?", (custom_path,))
    row = cur.fetchone()
    conn.close()
    assert row is not None and row[0] == custom_path

def test_task_func_duplicate_path(setup_database):
    path_to_append = "path/to/whatever"
    database = setup_database
    # Insert the path once
    task_func(path_to_append=path_to_append, database=database)
    # Try to insert the same path again
    result = task_func(path_to_append=path_to_append, database=database)
    assert result == path_to_append

    # Check if the path is still in the database
    conn = sqlite3.connect(database)
    cur = conn.cursor()
    cur.execute("SELECT * FROM paths WHERE path=?", (path_to_append,))
    rows = cur.fetchall()
    conn.close()
    assert len(rows) == 1 and rows[0][0] == path_to_append