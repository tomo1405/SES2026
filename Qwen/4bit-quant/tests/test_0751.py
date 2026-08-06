import pytest
from src_0751 import task_func
import pandas as pd
import numpy as np

@pytest.fixture
def sample_data():
    data = {
        'A': [1, 2, 3, 4, 5],
        'B': [10, 20, 30, 40, 50],
        'C': [50, 60, 70, 80, 90]
    }
    return pd.DataFrame(data)

def test_task_func_empty_dataframe(sample_data):
    empty_df = pd.DataFrame()
    result = task_func(empty_df, 25, 75, ['A', 'B', 'C'])
    assert result is None

def test_task_func_no_matching_rows(sample_data):
    result = task_func(sample_data, 50, 20, ['A', 'B', 'C'])
    assert result is None

def test_task_func_valid_input(sample_data):
    result = task_func(sample_data, 25, 75, ['A', 'B', 'C'])
    assert isinstance(result, pd.core.frame.DataFrame)

def test_task_func_invalid_columns(sample_data):
    with pytest.raises(KeyError):
        task_func(sample_data, 25, 75, ['D', 'E', 'F'])

def test_task_func_single_column(sample_data):
    with pytest.raises(IndexError):
        task_func(sample_data, 25, 75, ['A'])