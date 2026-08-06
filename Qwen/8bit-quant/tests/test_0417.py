import pytest
from src_0417 import task_func
import pandas as pd
import seaborn as sns

def test_task_func_no_column():
    data = {'a': [1, 2, 3], 'b': [4, 5, 6]}
    result = task_func(data)
    assert isinstance(result, sns.axisgrid.HeatMap)

def test_task_func_with_column():
    data = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}
    result = task_func(data, column='c')
    assert isinstance(result, sns.axisgrid.HeatMap)

def test_task_func_empty_data():
    data = {}
    result = task_func(data)
    assert result is None

def test_task_func_non_numeric_columns():
    data = {'a': ['x', 'y', 'z'], 'b': ['p', 'q', 'r']}
    result = task_func(data)
    assert result is None

def test_task_func_mixed_data_types():
    data = {'a': [1, 2, 3], 'b': ['p', 'q', 'r'], 'c': [7, 8, 9]}
    result = task_func(data, column='b')
    assert isinstance(result, sns.axisgrid.HeatMap)

def test_task_func_single_numeric_column():
    data = {'a': [1, 2, 3]}
    result = task_func(data)
    assert result is None