import pytest
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
    results = c.fetchall()

    assert len(results) == num_entries
    assert all(result[1] in users for result in results)
    assert all(result[2] in countries for result in results)
    assert all(result[3] in range(20, 60) for result in results)

    conn.close()