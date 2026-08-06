import pytest
from src_0517 import task_func
import pandas as pd
import numpy as np
import statsmodels.api as sm

def test_task_func_with_valid_input():
    # Define a valid input array
    array = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15]
    ]
    random_seed = 42

    # Call the function
    df, results = task_func(array, random_seed)

    # Check if the DataFrame is created correctly
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (3, 5)
    assert all(col in df.columns for col in ["A", "B", "C", "D", "Response"])

    # Check if the regression results are created correctly
    assert isinstance(results, sm.regression.linear_model.RegressionResultsWrapper)

def test_task_func_with_invalid_input_length():
    # Define an invalid input array with incorrect number of elements in a sub-list
    array = [
        [1, 2, 3, 4],  # Only 4 elements instead of 5
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15]
    ]
    random_seed = 42

    # Check if the function raises a ValueError
    with pytest.raises(ValueError, match="Each sub-list in the input 2D list must have exactly 5 elements."):
        task_func(array, random_seed)

def test_task_func_with_empty_input():
    # Define an empty input array
    array = []
    random_seed = 42

    # Call the function
    df, results = task_func(array, random_seed)

    # Check if the DataFrame is created correctly
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (0, 5)
    assert all(col in df.columns for col in ["A", "B", "C", "D", "Response"])

    # Check if the regression results are created correctly
    assert isinstance(results, sm.regression.linear_model.RegressionResultsWrapper)

def test_task_func_with_single_row_input():
    # Define a single row input array
    array = [
        [1, 2, 3, 4, 5]
    ]
    random_seed = 42

    # Call the function
    df, results = task_func(array, random_seed)

    # Check if the DataFrame is created correctly
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (1, 5)
    assert all(col in df.columns for col in ["A", "B", "C", "D", "Response"])

    # Check if the regression results are created correctly
    assert isinstance(results, sm.regression.linear_model.RegressionResultsWrapper)