python
import sys
import sqlite3
import pytest

# Constants
PATH_TO_APPEND = "path/to/whatever"
DATABASE = "path/to/database.db"

def task_func(path_to_append=PATH_TO_APPEND, database=DATABASE):
    sys.path.append(path_to_append)

    conn = sqlite3.connect(database)
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS paths (path TEXT UNIQUE)")
    cur.execute("INSERT OR IGNORE INTO paths (path) VALUES (?)", (path_to_append,))
    conn.commit()
    conn.close()

    return path_to_append

def test_task_func():
    # Test case 1: Default values
    assert task_func() == PATH_TO_APPEND

    # Test case 2: Custom values
    assert task_func("path/to/custom", "path/to/database.db") == "path/to/custom"