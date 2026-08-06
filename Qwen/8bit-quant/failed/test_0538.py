import pytest
from src_0538 import task_func
import pandas as pd
import sqlite3

@pytest.fixture
def create_test_db(tmp_path):
    db_path = tmp_path / "test.db"
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE People (id INTEGER PRIMARY KEY, age INTEGER)")
    cursor.executemany("INSERT INTO People (age) VALUES (?)", [(25,), (30,), (-1,)])
    conn.commit()
    conn.close()
    return db_path

def test_task_func_positive_ages(create_test_db):
    db_path = create_test_db
    with pytest.raises(ValueError) as exc_info:
        task_func(db_name=str(db_path))
    assert str(exc_info.value) == "Data contains negative age values."

def test_task_func_negative_ages(create_test_db):
    db_path = create_test_db
    cursor = sqlite3.connect(db_path).cursor()
    cursor.execute("DELETE FROM People WHERE age < 0")
    cursor.commit()
    
    ax = task_func(db_name=str(db_path))
    assert isinstance(ax, sns.axisgrid.FacetGrid)
    assert ax.get_xlabel() == "age"