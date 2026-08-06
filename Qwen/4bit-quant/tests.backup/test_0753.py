import pytest
from src_0753 import task_func
import pandas as pd
import numpy as np

def test_task_func_with_valid_data():
    # Create a sample DataFrame
    data = pd.DataFrame({
        'feature1': [1, 2, 3, 4, 5],
        'feature2': [5, 4, 3, 2, 1],
        'target': [2, 4, 6, 8, 10]
    })
    score = task_func(data, 'target', test_size=0.2, random_state=0)
    assert isinstance(score, float)
    assert 0 <= score <= 1

def test_task_func_with_non_dataframe_input():
    with pytest.raises(ValueError, match="data should be a DataFrame."):
        task_func([1, 2, 3], 'target')

def test_task_func_with_empty_dataframe():
    with pytest.raises(ValueError, match="data should contain at least one row."):
        task_func(pd.DataFrame(), 'target')

def test_task_func_with_missing_target_column():
    data = pd.DataFrame({'feature1': [1, 2, 3]})
    with pytest.raises(ValueError, match="target_column should be in the provided DataFrame."):
        task_func(data, 'target')

def test_task_func_with_non_numeric_data():
    data = pd.DataFrame({'feature1': ['a', 'b', 'c'], 'target': [1, 2, 3]})
    with pytest.raises(ValueError, match="data values should be numeric only."):
        task_func(data, 'target')

def test_task_func_with_invalid_test_size():
    data = pd.DataFrame({'feature1': [1, 2, 3], 'target': [1, 2, 3]})
    with pytest.raises(ValueError, match="test_size should be between 0 and 1: 0 < test_size < 1"):
        task_func(data, 'target', test_size=-0.1)
    with pytest.raises(ValueError, match="test_size should be between 0 and 1: 0 < test_size < 1"):
        task_func(data, 'target', test_size=1.1)

def test_task_func_with_non_integer_random_state():
    data = pd.DataFrame({'feature1': [1, 2, 3], 'target': [1, 2, 3]})
    with pytest.raises(ValueError, match="random_state should be an integer."):
        task_func(data, 'target', random_state='string')