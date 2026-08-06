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
    for row in rows:
        assert row[1] in users
        assert row[2] in range(20, 60)
        assert row[3] in countries

    conn.close()