import pytest
from src_0644 import task_func
import pandas as pd
import numpy as np

@pytest.fixture
def sample_dataframe():
    data = {
        'A': ['>12.34<', '>56.78<', None, '>90.12<'],
        'B': ['>34.56<', '>78.90<', '>12.34<', None]
    }
    return pd.DataFrame(data)

def test_task_func_with_valid_data(sample_dataframe):
    expected_output = pd.DataFrame({
        'A': [12.34, 56.78, np.nan, 90.12],
        'B': [34.56, 78.90, 12.34, np.nan]
    })
    result = task_func(sample_dataframe)
    pd.testing.assert_frame_equal(result, expected_output)

def test_task_func_with_no_matching_pattern():
    data = {
        'A': ['>abc<', '>def<', None, '>ghi<'],
        'B': ['>jkl<', '>mno<', '>pqr<', None]
    }
    df = pd.DataFrame(data)
    expected_output = pd.DataFrame({
        'A': [np.nan, np.nan, np.nan, np.nan],
        'B': [np.nan, np.nan, np.nan, np.nan]
    })
    result = task_func(df)
    pd.testing.assert_frame_equal(result, expected_output)

def test_task_func_with_empty_dataframe():
    df = pd.DataFrame(columns=['A', 'B'])
    expected_output = pd.DataFrame(columns=['A', 'B'])
    result = task_func(df)
    pd.testing.assert_frame_equal(result, expected_output)

def test_task_func_with_non_string_values():
    data = {
        'A': [12.34, 56.78, None, 90.12],
        'B': ['>34.56<', '>78.90<', '>12.34<', None]
    }
    df = pd.DataFrame(data)
    with pytest.raises(AttributeError):
        task_func(df)