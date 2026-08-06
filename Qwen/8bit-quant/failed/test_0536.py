import pytest
from src_0536 import task_func
import sqlite3
import os

@pytest.fixture
def db_path(tmpdir):
    return str(tmpdir.join("test.db"))

@pytest.fixture
def table_name():
    return "test_table"

@pytest.fixture
def cleanup(db_path, table_name):
    yield
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute(f"DROP TABLE IF EXISTS {table_name}")
    conn.commit()
    conn.close()

def test_task_func_positive(db_path, table_name, cleanup):
    num_entries = 5
    inserted_rows = task_func(db_path, table_name, num_entries)
    assert inserted_rows == num_entries

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute(f"SELECT COUNT(*) FROM {table_name}")
    count = cur.fetchone()[0]
    conn.close()
    assert count == num_entries

def test_task_func_zero_entries(db_path, table_name, cleanup):
    num_entries = 0
    inserted_rows = task_func(db_path, table_name, num_entries)
    assert inserted_rows == num_entries

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute(f"SELECT COUNT(*) FROM {table_name}")
    count = cur.fetchone()[0]
    conn.close()
    assert count == num_entries

def test_task_func_negative_entries(db_path, table_name):
    with pytest.raises(ValueError):
        task_func(db_path, table_name, -1)

def test_task_func_with_random_seed(db_path, table_name, cleanup):
    random_seed = 42
    num_entries = 5
    task_func(db_path, table_name, num_entries, random_seed)

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {table_name}")
    rows = cur.fetchall()
    conn.close()

    # Re-run with the same seed to ensure reproducibility
    task_func(db_path, table_name, num_entries, random_seed)
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {table_name}")
    rows_repeated = cur.fetchall()
    conn.close()

    assert rows == rows_repeated