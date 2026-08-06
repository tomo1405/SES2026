import sqlite3
from random import choice, seed
import os
import pytest

def task_func(db_name, table_name, num_entries, random_seed=None):
    NAMES = ["John", "Jane", "Steve", "Emma", "Liam", "Olivia"]
    AGES = range(18, 65)
    HEIGHTS = range(150, 200)

    if random_seed:
        seed(random_seed)

    if num_entries < 0:
        raise ValueError("num_entries must not be negative")

    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    cur.execute(f"CREATE TABLE {table_name} (name TEXT, age INTEGER, height INTEGER)")

    for _ in range(num_entries):
        name = choice(NAMES)
        age = choice(AGES)
        height = choice(HEIGHTS)
        cur.execute(f"INSERT INTO {table_name} VALUES (?, ?, ?)", (name, age, height))

    conn.commit()
    return os.path.abspath(db_name)

def test_task_func():
    db_name = "test.db"
    table_name = "test_table"
    num_entries = 5
    random_seed = 42
    seed(random_seed)
    expected_num_entries = 5
    expected_table_name = "test_table"
    expected_db_name = "test.db"
    result = task_func(db_name, table_name, num_entries, random_seed)
    assert result == os.path.abspath(expected_db_name)
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    cur.execute(f"SELECT COUNT(*) FROM {expected_table_name}")
    actual_num_entries = cur.fetchone()[0]
    assert actual_num_entries == expected_num_entries
    cur.execute(f"SELECT name FROM {expected_table_name} WHERE age = 22")
    actual_name = cur.fetchone()[0]
    assert actual_name in NAMES
    conn.close()
    os.remove(db_name)

if __name__ == "__main__":
    pytest.main()