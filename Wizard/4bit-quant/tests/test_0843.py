python
import sqlite3
import random
import pytest

from src_0843 import task_func

@pytest.fixture
def db_path():
    return 'test.db'

def test_task_func(db_path):
    num_entries = 10
    users = ['Alice', 'Bob', 'Charlie', 'Dave', 'Eve']
    countries = ['USA', 'UK', 'Canada', 'Australia', 'India']
    random_seed = 42

    task_func(db_path, num_entries, users, countries, random_seed)

    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    result = c.execute('SELECT * FROM users').fetchall()

    assert len(result) == num_entries

    for row in result:
        assert row[1] in users
        assert 20 <= row[2] <= 60
        assert row[3] in countries

    conn.close()