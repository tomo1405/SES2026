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
    choice_mock = unittest.mock.Mock(side_effect=[
        "John", "Jane", "Steve", "Emma", "Liam", "Olivia"
    ])
    seed_mock = unittest.mock.Mock()
    with unittest.mock.patch("random.choice", choice_mock), \
         unittest.mock.patch("random.seed", seed_mock), \
         unittest.mock.patch("numpy.random.seed", seed_mock):
        result = task_func(db_path, table_name, num_entries, random_seed)

    assert result == num_entries
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM {}".format(table_name))
    count = cur.fetchone()[0]
    assert count == num_entries