python
import sqlite3
import numpy as np
from random import choice, seed
import pytest

def task_func(db_path, table_name, num_entries, random_seed=None):
    # Setting the random seed if provided
    if random_seed is not None:
        seed(random_seed)
        np.random.seed(random_seed)

    if num_entries < 0:
        raise ValueError("num_entries cannot be negative.")

    NAMES = ["John", "Jane", "Steve", "Emma", "Liam", "Olivia"]
    AGES = list(range(18, 65))
    HEIGHTS = list(range(150, 200))

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    table_creation_sql = (
        "CREATE TABLE IF NOT EXISTS {} (name TEXT, age INTEGER, height INTEGER)".format(
            table_name
        )
    )
    cur.execute(table_creation_sql)

    inserted_rows = 0
    for _ in range(num_entries):
        name = choice(NAMES)
        age = choice(AGES)
        height = choice(HEIGHTS)
        insertion_sql = "INSERT INTO {} VALUES (?, ?, ?)".format(table_name)
        cur.execute(insertion_sql, (name, age, height))
        inserted_rows += cur.rowcount

    conn.commit()

    return inserted_rows

def test_task_func():
    # Test case 1: Test with valid inputs
    assert task_func("test.db", "test_table", 10) == 10

    # Test case 2: Test with negative num_entries
    with pytest.raises(ValueError):
        task_func("test.db", "test_table", -10)

    # Test case 3: Test with non-existent db_path
    with pytest.raises(sqlite3.OperationalError):
        task_func("non_existent.db", "test_table", 10)

    # Test case 4: Test with non-existent table_name
    with pytest.raises(sqlite3.OperationalError):
        task_func("test.db", "non_existent_table", 10)

    # Test case 5: Test with random_seed
    assert task_func("test.db", "test_table", 10, random_seed=42) == 10

    # Test case 6: Test with num_entries=0
    assert task_func("test.db", "test_table", 0) == 0