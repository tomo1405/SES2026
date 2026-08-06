import numpy as np
import pandas as pd
import pytest
from src_0229 import task_func

# Constants
COLUMNS = ['column1', 'column2', 'column3', 'column4', 'column5']

def test_task_func_valid_input():
    """
    Test if the function raises an exception when the input is not a DataFrame.
    """
    df = "not a DataFrame"
    dct = {"old_value": "new_value"}
    with pytest.raises(ValueError) as excinfo:
        task_func(df, dct)
    assert "The input df is not a DataFrame" in str(excinfo.value)

def test_task_func_replace_values():
    """
    Test if the function replaces values in the DataFrame using the dictionary mapping.
    """
    df = pd.DataFrame({"column1": [1, 2, 3], "column2": [4, 5, 6], "column3": [7, 8, 9]})
    dct = {"1": "one", "2": "two", "3": "three"}
    expected_df = pd.DataFrame({"column1": ["one", "two", "three"], "column2": ["four", "five", "six"], "column3": ["seven", "eight", "nine"]})
    actual_df = task_func(df, dct)
    assert actual_df.equals(expected_df)

def test_task_func_calculate_correlation_matrix():
    """
    Test if the function calculates the correlation matrix correctly.
    """
    df = pd.DataFrame({"column1": [1, 2, 3], "column2": [4, 5, 6], "column3": [7, 8, 9]})
    dct = {}
    expected_matrix = np.array([[1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [1.0, 1.0, 1.0]])
    actual_matrix = task_func(df, dct).values
    assert np.array_equal(actual_matrix, expected_matrix)