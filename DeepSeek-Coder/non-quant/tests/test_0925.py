import pytest
from src_0925 import task_func
import pandas as pd
import os

# Test cases for the task_func function

def test_file_not_found():
    with pytest.raises(SystemExit) as e:
        task_func("nonexistent_file.csv", "column_name")
    assert str(e.value) == "1"

def test_column_exists():
    df = pd.DataFrame({
        'column1': [1, 2, 3],
        'column2': ['a', 'b', 'c']
    })
    result = task_func("test_file.csv", "column1")
    assert result.equals(df)

def test_column_not_exists():
    with pytest.raises(SystemExit) as e:
        task_func("test_file.csv", "nonexistent_column")
    assert str(e.value) == "1"