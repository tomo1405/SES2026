import pytest
from src_0706 import task_func
import numpy as np
import pandas as pd

# Sample DataFrame for testing
@pytest.fixture
def sample_data():
    data = {
        'column1': [1, 2, 3, 4, 5],
        'column2': [5, 4, 3, 2, 1]
    }
    return pd.DataFrame(data)

def test_task_func(sample_data):
    df = sample_data
    column = 'column1'
    alpha = 0.05
    result = task_func(df, column, alpha)
    assert isinstance(result, bool), "The function should return a boolean value."

def test_task_func_column_not_exist(sample_data):
    df = sample_data
    column = 'non_existent_column'
    alpha = 0.05
    with pytest.raises(ValueError):
        task_func(df, column, alpha)

def test_task_func_with_large_alpha(sample_data):
    df = sample_data
    column = 'column1'
    alpha = 0.9  # Greater than 0.05
    result = task_func(df, column, alpha)
    assert result, "The function should return True if p-value is greater than alpha."

def test_task_func_with_small_alpha(sample_data):
    df = sample_data
    column = 'column1'
    alpha = 0.01  # Less than 0.05
    result = task_func(df, column, alpha)
    assert not result, "The function should return False if p-value is less than alpha."