import sqlite3
import random
import pytest
from src_0843 import task_func

def test_task_func():
    db_path = 'test.db'
    num_entries = 10
    random_seed = 42
    users = ['Alice', 'Bob', 'Charlie', 'Dave', 'Eve']
    countries = ['USA', 'UK', 'Canada', 'Australia', 'India']

    task_func(db_path, num_entries, users, countries, random_seed)

    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('SELECT COUNT(*) FROM users')
    count = c.fetchone()[0]
    conn.close()

    assert count == num_entries, 'Number of entries in the database does not match the expected value'

def test_task_func_with_default_args():
    db_path = 'test.db'
    num_entries = 5
    task_func(db_path, num_entries)

    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('SELECT COUNT(*) FROM users')
    count = c.fetchone()[0]
    conn.close()

    assert count == num_entries, 'Number of entries in the database does not match the expected value'