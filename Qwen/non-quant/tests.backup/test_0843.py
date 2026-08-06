import pytest
from src_0843 import task_func
import os
import sqlite3

@pytest.fixture
def temp_db_path(tmpdir):
    return str(tmpdir / "temp.db")

def test_task_func(temp_db_path):
    num_entries = 10
    random_seed = 42
    task_func(temp_db_path, num_entries, random_seed=random_seed)

    conn = sqlite3.connect(temp_db_path)
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    rows = c.fetchall()
    conn.close()

    assert len(rows) == num_entries

    expected_users = ['Alice', 'Bob', 'Charlie', 'Dave', 'Eve']
    expected_countries = ['USA', 'UK', 'Canada', 'Australia', 'India']

    for row in rows:
        assert row[1] in expected_users
        assert 20 <= row[2] <= 60
        assert row[3] in expected_countries

def test_task_func_no_entries(temp_db_path):
    num_entries = 0
    task_func(temp_db_path, num_entries)

    conn = sqlite3.connect(temp_db_path)
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    rows = c.fetchall()
    conn.close()

    assert len(rows) == num_entries

def test_task_func_with_custom_users_and_countries(temp_db_path):
    num_entries = 5
    custom_users = ['Tom', 'Jerry']
    custom_countries = ['France', 'Germany']
    task_func(temp_db_path, num_entries, users=custom_users, countries=custom_countries)

    conn = sqlite3.connect(temp_db_path)
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    rows = c.fetchall()
    conn.close()

    assert len(rows) == num_entries

    for row in rows:
        assert row[1] in custom_users
        assert 20 <= row[2] <= 60
        assert row[3] in custom_countries

def test_task_func_id_autoincrement(temp_db_path):
    num_entries = 3
    task_func(temp_db_path, num_entries)

    conn = sqlite3.connect(temp_db_path)
    c = conn.cursor()
    c.execute("SELECT id FROM users ORDER BY id")
    ids = [row[0] for row in c.fetchall()]
    conn.close()

    assert ids == list(range(1, num_entries + 1))

def test_task_func_repeated_calls(temp_db_path):
    num_entries = 2
    task_func(temp_db_path, num_entries)
    task_func(temp_db_path, num_entries)

    conn = sqlite3.connect(temp_db_path)
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    rows = c.fetchall()
    conn.close()

    assert len(rows) == num_entries * 2

def test_task_func_db_file_exists(temp_db_path):
    task_func(temp_db_path, 1)
    assert os.path.exists(temp_db_path)