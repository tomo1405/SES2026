import sqlite3
import pandas as pd
import pytest
from src_0539 import task_func

def test_task_func():
    db_name = "example.db"
    table_name = "example_table"
    conn = sqlite3.connect(db_name)
    df = pd.read_sql_query(f"SELECT * from {table_name}", conn)
    numerical_columns = df.select_dtypes(include=["float64", "int64"]).columns.tolist()
    if "id" in numerical_columns:
        numerical_columns.remove("id")
    if len(numerical_columns) < 2:
        with pytest.raises(ValueError) as excinfo:
            task_func(db_name, table_name)
        assert "The table must have at least two numerical columns to plot." in str(excinfo.value)
    else:
        ax = task_func(db_name, table_name)
        assert ax is not None