python
import sqlite3
import random
import os
import pytest

from src_0540 import task_func

def test_task_func():
    db_name = "test.db"
    table_name = "test_table"
    num_entries = 10
    random_seed = 42

    task_func(db_name, table_name, num_entries, random_seed)

    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    cur.execute(f"SELECT COUNT(*) FROM {table_name}")
    count = cur.fetchone()[0]
    assert count == num_entries

    conn.close()
    os.remove(db_name)