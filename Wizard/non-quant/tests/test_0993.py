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
    assert task_func() == PATH_TO_APPEND

def test_task_func_with_path_arg():
    assert task_func(path_to_append="new/path") == "new/path"

def test_task_func_with_database_arg():
    assert task_func(database="new/database.db") == PATH_TO_APPEND

def test_task_func_with_both_args():
    assert task_func(path_to_append="new/path", database="new/database.db") == "new/path"