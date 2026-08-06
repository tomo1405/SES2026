import sqlite3

import pytest
import seaborn as sns
from src_0538 import task_func


@pytest.fixture
def setup_database(tmp_path):
    db_path = tmp_path / "test.db"
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE People (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")
    cursor.execute("INSERT INTO People (name, age) VALUES ('Alice', 30), ('Bob', 25), ('Charlie', -1)")
    conn.commit()
    conn.close()
    return str(db_path)

def test_task_func_positive_ages(setup_database):
    db_path = setup_database
    with pytest.raises(ValueError):
        task_func(db_path, "People")

def test_task_func_valid_data(tmp_path):
    db_path = tmp_path / "test.db"
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE People (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")
    cursor.execute("INSERT INTO People (name, age) VALUES ('Alice', 30), ('Bob', 25), ('Charlie', 40)")
    conn.commit()
    conn.close()

    ax = task_func(str(db_path), "People")
    assert isinstance(ax, sns.axisgrid.FacetGrid)

def test_task_func_no_data(tmp_path):
    db_path = tmp_path / "test.db"
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE People (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")
    conn.commit()
    conn.close()

    ax = task_func(str(db_path), "People")
    assert isinstance(ax, sns.axisgrid.FacetGrid)