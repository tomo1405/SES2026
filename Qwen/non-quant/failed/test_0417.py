import pytest
from src_0417 import task_func
import pandas as pd
import numpy as np

def test_task_func_with_valid_data():
    data = {
        'a': [1, 2, 3],
        'b': [4, 5, 6],
        'c': [7, 8, 9]
    }
    result = task_func(data)
    assert isinstance(result, pd.DataFrame)

def test_task_func_with_missing_column():
    data = {
        'a': [1, 2, 3],
        'b': [4, 5, 6]
    }
    result = task_func(data, column='c')
    assert result is None

def test_task_func_with_non_numeric_columns():
    data = {
        'a': ['x', 'y', 'z'],
        'b': [4, 5, 6]
    }
    result = task_func(data)
    assert result is None

def test_task_func_with_empty_data():
    data = {}
    result = task_func(data)
    assert result is None

def test_task_func_with_all_numeric_data():
    data = {
        'a': [1, 2, 3],
        'b': [4, 5, 6],
        'c': [7, 8, 9]
    }
    result = task_func(data, column='c')
    assert isinstance(result, pd.DataFrame)

def test_task_func_with_single_column():
    data = {
        'a': [1, 2, 3]
    }
    result = task_func(data)
    assert result is None