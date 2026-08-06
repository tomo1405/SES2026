import pytest
from src_0843 import task_func
import os
import sqlite3

@pytest.fixture
def temp_db_path(tmpdir):
    return str(tmpdir / "test.db")

def test_task_func(temp_db_path):
    # Test with default parameters
    db_path = task_func(temp_db_path, 5)
    assert os.path.exists(db_path)

    # Check if the database has been created and contains the correct table
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users'")
    assert c.fetchone() is not None

    # Check if the correct number of entries have been inserted
    c.execute("SELECT COUNT(*) FROM users")
    count = c.fetchone()[0]
    assert count == 5

    # Check if the entries have the correct columns
    c.execute("PRAGMA table_info(users)")
    columns = [row[1] for row in c.fetchall()]
    assert columns == ['id', 'name', 'age', 'country']

    # Clean up
    conn.close()
    os.remove(db_path)

def test_task_func_with_random_seed(temp_db_path):
    # Test with a specific random seed
    db_path = task_func(temp_db_path, 5, random_seed=42)
    assert os.path.exists(db_path)

    # Check if the database has been created and contains the correct table
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users'")
    assert c.fetchone() is not None

    # Check if the correct number of entries have been inserted
    c.execute("SELECT COUNT(*) FROM users")
    count = c.fetchone()[0]
    assert count == 5

    # Check if the entries have the correct columns
    c.execute("PRAGMA table_info(users)")
    columns = [row[1] for row in c.fetchall()]
    assert columns == ['id', 'name', 'age', 'country']

    # Clean up
    conn.close()
    os.remove(db_path)