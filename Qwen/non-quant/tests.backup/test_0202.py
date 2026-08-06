import pytest
from src_0202 import task_func
import pandas as pd
import numpy as np

@pytest.fixture
def sample_df():
    data = {
        'A': [1, 2, 3, 4, 5],
        'B': [10, 20, 30, 40, 50]
    }
    return pd.DataFrame(data)

def test_task_func_column_not_exists(sample_df):
    with pytest.raises(ValueError, match="Column 'C' does not exist in DataFrame"):
        task_func(sample_df, 'C', 3)

def test_task_func_value_not_number(sample_df):
    with pytest.raises(ValueError, match="Value must be a number"):
        task_func(sample_df, 'A', 'three')

def test_task_func_valid_input(sample_df):
    greater_avg, num_greater_value, ax = task_func(sample_df, 'A', 3)
    expected_greater_avg = np.array([4, 5])
    expected_num_greater_value = 2
    assert np.array_equal(greater_avg, expected_greater_avg)
    assert num_greater_value == expected_num_greater_value
    assert ax is not None

def test_task_func_all_values_greater_than_average(sample_df):
    greater_avg, num_greater_value, ax = task_func(sample_df, 'A', 0)
    expected_greater_avg = np.array([1, 2, 3, 4, 5])
    expected_num_greater_value = 0
    assert np.array_equal(greater_avg, expected_greater_avg)
    assert num_greater_value == expected_num_greater_value
    assert ax is not None

def test_task_func_all_values_less_than_average(sample_df):
    greater_avg, num_greater_value, ax = task_func(sample_df, 'A', 6)
    expected_greater_avg = np.array([])
    expected_num_greater_value = 5
    assert np.array_equal(greater_avg, expected_greater_avg)
    assert num_greater_value == expected_num_greater_value
    assert ax is not None