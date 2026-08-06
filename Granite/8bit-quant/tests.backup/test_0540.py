import sqlite3
from random import choice, seed
import os
from src_0540 import task_func
import pytest

NAMES = ["John", "Jane", "Steve", "Emma", "Liam", "Olivia"]
AGES = range(18, 65)
HEIGHTS = range(150, 200)

def test_task_func():
    db_name = "test.db"
    table_name = "test_table"
    num_entries = 5
    random_seed = 42

    seed(random_seed)

    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    cur.execute(f"CREATE TABLE {table_name} (name TEXT, age INTEGER, height INTEGER)")

    for _ in range(num_entries):
        name = choice(NAMES)
        age = choice(AGES)
        height = choice(HEIGHTS)
        cur.execute(f"INSERT INTO {table_name} VALUES (?, ?, ?)", (name, age, height))

    conn.commit()
    result = task_func(db_name, table_name, num_entries, random_seed)
    expected_result = os.path.abspath(db_name)
    assert result == expected_result

def test_task_func_invalid_num_entries():
    db_name = "test.db"
    table_name = "test_table"
    num_entries = -1
    random_seed = 42

    with pytest.raises(ValueError) as excinfo:
        task_func(db_name, table_name, num_entries, random_seed)
    assert "num_entries must not be negative" in str(excinfo.value)