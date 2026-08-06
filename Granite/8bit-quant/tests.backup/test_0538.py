import sqlite3
import pandas as pd
import seaborn as sns
import pytest

from src_0538 import task_func

def test_task_func_with_valid_input():
    db_name = "test.db"
    table_name = "People"
    conn = sqlite3.connect(db_name)
    df = pd.read_sql_query(f"SELECT age from {table_name}", conn)
    ax = sns.histplot(data=df, x="age", bins=30, kde=True)
    ax.set_xlabel("age")
    assert task_func(db_name, table_name) == ax

def test_task_func_with_invalid_input():
    db_name = "test.db"
    table_name = "People"
    conn = sqlite3.connect(db_name)
    df = pd.read_sql_query(f"SELECT age from {table_name}", conn)
    df.loc[0, "age"] = -1
    with pytest.raises(ValueError, match="Data contains negative age values."):
        task_func(db_name, table_name)