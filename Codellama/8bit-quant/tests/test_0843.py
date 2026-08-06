import sqlite3

from src_0843 import task_func


def test_task_func():
    db_path = 'test_db.db'
    num_entries = 10
    users = ['Alice', 'Bob', 'Charlie', 'Dave', 'Eve']
    countries = ['USA', 'UK', 'Canada', 'Australia', 'India']
    random_seed = 42

    task_func(db_path, num_entries, users, countries, random_seed)

    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    c.execute('SELECT * FROM users')
    rows = c.fetchall()

    assert len(rows) == num_entries
    assert all(row[1] in users for row in rows)
    assert all(row[2] in countries for row in rows)

    conn.close()