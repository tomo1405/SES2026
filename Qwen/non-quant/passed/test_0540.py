import pytest
from src_0540 import task_func
import os
import sqlite3

def test_task_func_positive_entries():
    db_name = "test_db.sqlite"
    table_name = "test_table"
    num_entries = 5
    random_seed = 42

    result = task_func(db_name, table_name, num_entries, random_seed)
    assert os.path.abspath(db_name) == result

    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    cur.execute(f"SELECT COUNT(*) FROM {table_name}")
    count = cur.fetchone()[0]
    assert count == num_entries

    cur.execute(f"SELECT * FROM {table_name}")
    rows = cur.fetchall()
    for row in rows:
        assert row[0] in ["John", "Jane", "Steve", "Emma", "Liam", "Olivia"]
        assert 18 <= row[1] <= 64
        assert 150 <= row[2] <= 199

    conn.close()
    os.remove(db_name)

def test_task_func_zero_entries():
    db_name = "test_db.sqlite"
    table_name = "test_table"
    num_entries = 0
    random_seed = 42

    result = task_func(db_name, table_name, num_entries, random_seed)
    assert os.path.abspath(db_name) == result

    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    cur.execute(f"SELECT COUNT(*) FROM {table_name}")
    count = cur.fetchone()[0]
    assert count == num_entries

    conn.close()
    os.remove(db_name)

def test_task_func_negative_entries():
    db_name = "test_db.sqlite"
    table_name = "test_table"
    num_entries = -1

    with pytest.raises(ValueError):
        task_func(db_name, table_name, num_entries)

def test_task_func_no_random_seed():
    db_name = "test_db.sqlite"
    table_name = "test_table"
    num_entries = 5

    result = task_func(db_name, table_name, num_entries)
    assert os.path.abspath(db_name) == result

    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    cur.execute(f"SELECT COUNT(*) FROM {table_name}")
    count = cur.fetchone()[0]
    assert count == num_entries

    conn.close()
    os.remove(db_name)