import sqlite3
import numpy as np
from random import choice, seed
from src_0536 import task_func
import pytest

def test_task_func():
    db_path = "test.db"
    table_name = "test_table"
    num_entries = 10
    random_seed = 42

    # Mock the random functions to make the test deterministic
    seed(random_seed)
    np.random.seed(random_seed)
    choice_mock = lambda x: x[0]  # Choose the first element of the list

    inserted_rows = task_func(db_path, table_name, num_entries, random_seed)

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM {}".format(table_name))
    num_rows = cur.fetchone()[0]

    assert inserted_rows == num_rows

    conn.close()

if __name__ == "__main__":
    pytest.main()