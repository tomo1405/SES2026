import sqlite3
import pandas as pd
import seaborn as sns
from src_0538 import task_func
import pytest

def test_task_func_with_valid_input():
    conn = sqlite3.connect("test.db")
    df = pd.DataFrame({"age": [20, 30, 40, 50]})
    conn.execute("CREATE TABLE People (age INTEGER)")
    df.to_sql("People", conn, if_exists="replace")
    ax = task_func(db_name="test.db", table_name="People")
    assert ax is not None

def test_task_func_with_invalid_input():
    conn = sqlite3.connect("test.db")
    df = pd.DataFrame({"age": [-10, 20, 30, 40, 50]})
    conn.execute("CREATE TABLE People (age INTEGER)")
    df.to_sql("People", conn, if_exists="replace")
    with pytest.raises(ValueError) as excinfo:
        task_func(db_name="test.db", table_name="People")
    assert "Data contains negative age values." in str(excinfo.value)