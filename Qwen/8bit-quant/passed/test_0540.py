import pytest
from src_0540 import task_func
import os
import sqlite3

@pytest.fixture
def temp_db_file():
    db_name = "test.db"
    yield db_name
    if os.path.exists(db_name):
        os.remove(db_name)

def test_task_func(temp_db_file):
    table_name = "test_table"
    num_entries = 5
    random_seed = 42

    result = task_func(temp_db_file, table_name, num_entries, random_seed)
    assert result == os.path.abspath(temp_db_file)

    conn = sqlite3.connect(result)
    cur = conn.cursor()
    cur.execute(f"SELECT COUNT(*) FROM {table_name}")
    count = cur.fetchone()[0]
    assert count == num_entries

    cur.execute(f"SELECT * FROM {table_name}")
    rows = cur.fetchall()
    assert len(rows) == num_entries

    for row in rows:
        name, age, height = row
        assert name in ["John", "Jane", "Steve", "Emma", "Liam", "Olivia"]
        assert 18 <= age <= 64
        assert 150 <= height <= 199

    conn.close()

def test_task_func_negative_entries(temp_db_file):
    with pytest.raises(ValueError):
        task_func(temp_db_file, "test_table", -1)

def test_task_func_no_seed(temp_db_file):
    table_name = "test_table"
    num_entries = 5

    result = task_func(temp_db_file, table_name, num_entries)
    assert result == os.path.abspath(temp_db_file)

    conn = sqlite3.connect(result)
    cur = conn.cursor()
    cur.execute(f"SELECT COUNT(*) FROM {table_name}")
    count = cur.fetchone()[0]
    assert count == num_entries

    cur.execute(f"SELECT * FROM {table_name}")
    rows = cur.fetchall()
    assert len(rows) == num_entries

    for row in rows:
        name, age, height = row
        assert name in ["John", "Jane", "Steve", "Emma", "Liam", "Olivia"]
        assert 18 <= age <= 64
        assert 150 <= height <= 199

    conn.close()