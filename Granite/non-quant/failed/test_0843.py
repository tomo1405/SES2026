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

    random.seed(random_seed)

    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    c.execute('''
        CREATE TABLE users
        (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, country TEXT)
    ''')

    for _ in range(num_entries):
        user = random.choice(users)
        age = random.randint(20, 60)
        country = random.choice(countries)
        c.execute('INSERT INTO users (name, age, country) VALUES (?, ?, ?)', (user, age, country))

    conn.commit()
    conn.close()

    result = task_func(db_path, num_entries, users, countries, random_seed)

    assert result == 'test.db'