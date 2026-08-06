import pytest
from src_0927 import task_func
import pandas as pd
import sqlite3

def test_task_func():
    db_path = "test.db"
    table_name = "test_table"
    column_name = "test_column"
    df = pd.DataFrame({"test_column": ["test\nvalue"]})
    df.to_sql(table_name, sqlite3.connect(db_path), if_exists="replace", index=False)
    result = task_func(db_path, table_name, column_name)
    assert result.equals(pd.DataFrame({"test_column": ["test<br>value"]}))
    assert result.dtypes[column_name] == "object"