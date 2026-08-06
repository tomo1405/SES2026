python
import sqlite3
import numpy as np
from random import choice, seed
import pytest

from src_0536 import task_func

def test_task_func_valid_inputs():
    # Test valid inputs
    db_path = "test.db"
    table_name = "test_table"
    num_entries = 10
    random_seed = 42

    inserted_rows = task_func(db_path, table_name, num_entries, random_seed)

    assert inserted_rows == num_entries

    # Check if the data was inserted correctly
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("SELECT * FROM {}".format(table_name))
    rows = cur.fetchall()
    conn.close()

    assert len(rows) == num_entries
    for row in rows:
        assert row[0] in ["John", "Jane", "Steve", "Emma", "Liam", "Olivia"]
        assert 18 <= row[1] <= 64
        assert 150 <= row[2] <= 199

def test_task_func_invalid_inputs():
    # Test invalid inputs
    db_path = "test.db"
    table_name = "test_table"
    num_entries = -10
    random_seed = 42

    with pytest.raises(ValueError):
        task_func(db_path, table_name, num_entries, random_seed)

    # Test if the database file was created
    assert not os.path.exists(db_path)