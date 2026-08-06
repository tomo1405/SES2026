import sqlite3
import pandas as pd
import seaborn as sns
import pytest

def task_func(db_name="test.db", table_name="People"):
    conn = sqlite3.connect(db_name)
    df = pd.read_sql_query(f"SELECT age from {table_name}", conn)

    if (df["age"] < 0).any():
        raise ValueError("Data contains negative age values.")

    ax = sns.histplot(data=df, x="age", bins=30, kde=True)
    ax.set_xlabel("age")
    return ax

def test_task_func():
    with pytest.raises(ValueError):
        task_func(table_name="InvalidTable")

    with pytest.raises(ValueError):
        task_func(db_name="InvalidDB.db")

    ax = task_func()
    assert ax.get_xlabel() == "age"