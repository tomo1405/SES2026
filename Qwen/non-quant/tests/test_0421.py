import pytest
from src_0421 import task_func
import pandas as pd
import numpy as np

@pytest.fixture
def sample_data():
    return {
        'A': [1, 2, 3],
        'B': ['4', '5', '6'],
        'C': ['7', 'eight', '9']
    }

def test_task_func_with_numeric_columns(sample_data):
    expected_output = pd.DataFrame({
        'A': [0.0, 1.0, 2.0],
        'B': [-1.22474487, 0.0, 1.22474487],
        'C': [np.nan, np.nan, np.nan]
    })
    result = task_func(sample_data)
    pd.testing.assert_frame_equal(result, expected_output)

def test_task_func_with_non_numeric_columns(sample_data):
    sample_data['D'] = ['ten', 'eleven', 'twelve']
    expected_output = pd.DataFrame({
        'A': [0.0, 1.0, 2.0],
        'B': [-1.22474487, 0.0, 1.22474487],
        'C': [np.nan, np.nan, np.nan],
        'D': [np.nan, np.nan, np.nan]
    })
    result = task_func(sample_data)
    pd.testing.assert_frame_equal(result, expected_output)

def test_task_func_with_all_non_numeric_columns():
    sample_data = {
        'A': ['one', 'two', 'three'],
        'B': ['four', 'five', 'six']
    }
    expected_output = pd.DataFrame({
        'A': [np.nan, np.nan, np.nan],
        'B': [np.nan, np.nan, np.nan]
    })
    result = task_func(sample_data)
    pd.testing.assert_frame_equal(result, expected_output)

def test_task_func_with_empty_dataframe():
    sample_data = {}
    expected_output = pd.DataFrame()
    result = task_func(sample_data)
    pd.testing.assert_frame_equal(result, expected_output)