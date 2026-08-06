import pytest
from src_0540 import task_func
import sqlite3
import os
from random import seed

@pytest.fixture
def setup_and_teardown():
    db_name = "test_db.db"
    table_name = "test_table"
    num_entries = 5
    random_seed = 42
    yield task_func(db_name, table_name, num_entries, random_seed)
    os.remove(db_name)

def test_task_func(setup_and_teardown):
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    cur.execute("SELECT * FROM test_table")
    results = cur.fetchall()
    assert len(results) == num_entries
    conn.close()