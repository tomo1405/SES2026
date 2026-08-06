import pytest
from src_0536 import task_func
import sqlite3
import os

@pytest.fixture
def temp_db_path():
    db_path = "temp_test.db"
    yield db_path
    os.remove(db_path)

def test_task_func_with_zero_entries(temp_db_path):
    table_name = "test_table"
    num_entries = 0
    result = task_func(temp_db_path, table_name, num_entries)
    assert result == 0

def test_task_func_with_positive_entries(temp_db_path):
    table_name = "test_table"
    num_entries = 5
    result = task_func(temp_db_path, table_name, num_entries)
    assert result == num_entries

    conn = sqlite3.connect(temp_db_path)
    cur = conn.cursor()
    cur.execute(f"SELECT COUNT(*) FROM {table_name}")
    count = cur.fetchone()[0]
    conn.close()
    assert count == num_entries

def test_task_func_with_negative_entries(temp_db_path):
    table_name = "test_table"
    num_entries = -1
    with pytest.raises(ValueError) as excinfo:
        task_func(temp_db_path, table_name, num_entries)
    assert str(excinfo.value) == "num_entries cannot be negative."

def test_task_func_with_random_seed(temp_db_path):
    table_name = "test_table"
    num_entries = 5
    random_seed = 42

    task_func(temp_db_path, table_name, num_entries, random_seed=random_seed)

    conn = sqlite3.connect(temp_db_path)
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {table_name}")
    rows = cur.fetchall()
    conn.close()

    expected_names = ["Liam"] * num_entries  # Based on the random seed 42
    expected_ages = [30] * num_entries      # Based on the random seed 42
    expected_heights = [175] * num_entries   # Based on the random seed 42

    assert [row[0] for row in rows] == expected_names
    assert [row[1] for row in rows] == expected_ages
    assert [row[2] for row in rows] == expected_heights

def test_task_func_table_creation(temp_db_path):
    table_name = "test_table"
    num_entries = 0
    task_func(temp_db_path, table_name, num_entries)

    conn = sqlite3.connect(temp_db_path)
    cur = conn.cursor()
    cur.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'")
    table_exists = cur.fetchone() is not None
    conn.close()
    assert table_exists