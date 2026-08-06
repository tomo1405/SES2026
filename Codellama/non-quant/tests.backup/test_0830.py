import pytest
from src_0830 import task_func
import pandas as pd

def test_task_func():
    df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'], 'Score': [100, 90, 80]})
    result = task_func(df)
    assert result == {'Alice': [(100, 100)], 'Bob': [(90, 90)], 'Charlie': [(80, 80)]}

def test_task_func_invalid_columns():
    df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'], 'Score': [100, 90, 80]})
    with pytest.raises(ValueError):
        task_func(df)