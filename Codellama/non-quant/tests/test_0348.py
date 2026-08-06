import pytest
from src_0348 import task_func
import pandas as pd
import numpy as np

def test_task_func():
    df = pd.DataFrame({'column': ['abcdefghijklmnopqrstuvwxyz', '1234567890', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']})
    result = task_func(df, 'column')
    expected = pd.Series({'abcdefghijklmnopqrstuvwxyz': 1, '1234567890': 1, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ': 1})
    pd.testing.assert_series_equal(result, expected)

def test_task_func_with_empty_column():
    df = pd.DataFrame({'column': []})
    result = task_func(df, 'column')
    expected = pd.Series()
    pd.testing.assert_series_equal(result, expected)

def test_task_func_with_invalid_column():
    df = pd.DataFrame({'column': ['abcdefghijklmnopqrstuvwxyz', '1234567890', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']})
    with pytest.raises(ValueError):
        task_func(df, 'invalid_column')