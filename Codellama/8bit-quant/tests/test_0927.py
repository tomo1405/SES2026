import sqlite3

import pandas as pd
import pytest
from src_0927 import task_func


def test_task_func():
    db_path = "test.db"
    table_name = "test_table"
    column_name = "test_column"
    df = pd.DataFrame({"test_column": ["\n", "test", "test\ntest"]})
    expected_df = pd.DataFrame({"test_column": ["<br>", "test", "test<br>test"]})
    with pytest.raises(sqlite3.OperationalError):
        task_func(db_path, table_name, column_name)
    assert df.equals(expected_df)