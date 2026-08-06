import pytest
from src_0830 import task_func
import pandas as pd

def test_task_func():
    df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'], 'Score': [10, 20, 30]})
    result = task_func(df)
    assert result == {'Alice': [(10, 10)], 'Bob': [(20, 20)], 'Charlie': [(30, 30)]}

def test_task_func_invalid_input():
    df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'], 'Score': [10, 20, 30]})
    with pytest.raises(ValueError):
        task_func(df[['Name', 'Score']])