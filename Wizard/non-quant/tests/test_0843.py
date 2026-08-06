python
import sqlite3
import random
import pytest

from src_0843 import task_func

def test_task_func():
    db_path = 'test.db'
    num_entries = 10
    users = ['Alice', 'Bob', 'Charlie', 'Dave', 'Eve']
    countries = ['USA', 'UK', 'Canada', 'Australia', 'India']
    random_seed = 42

    task_func(db_path, num_entries, users, countries, random_seed)

    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    c.execute('SELECT COUNT(*) FROM users')
    assert c.fetchone()[0] == num_entries

    c.execute('SELECT name, age, country FROM users ORDER BY id')
    rows = c.fetchall()
    for i in range(num_entries):
        assert rows[i][0] in users
        assert 20 <= rows[i][1] <= 60
        assert rows[i][2] in countries

    conn.close()