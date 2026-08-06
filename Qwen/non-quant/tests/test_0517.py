import pandas as pd
import pytest
from src_0517 import task_func


def test_task_func_valid_input():
    # Test with a valid input
    data = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15]
    ]
    df, results = task_func(data, random_seed=42)
    
    # Check if the DataFrame is created correctly
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (3, 5)
    assert list(df.columns) == ["A", "B", "C", "D", "Response"]
    
    # Check if the regression results are returned
    assert isinstance(results, sm.regression.linear_model.RegressionResultsWrapper)

def test_task_func_invalid_input_length():
    # Test with invalid input where sub-lists do not have 5 elements
    data = [
        [1, 2, 3, 4],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15]
    ]
    with pytest.raises(ValueError, match="Each sub-list in the input 2D list must have exactly 5 elements."):
        task_func(data, random_seed=42)

def test_task_func_empty_input():
    # Test with empty input
    data = []
    df, results = task_func(data, random_seed=42)
    
    # Check if the DataFrame is created correctly
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (0, 5)
    assert list(df.columns) == ["A", "B", "C", "D", "Response"]
    
    # Check if the regression results are returned
    assert isinstance(results, sm.regression.linear_model.RegressionResultsWrapper)

def test_task_func_random_seed_consistency():
    # Test to ensure that the random seed produces consistent results
    data = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15]
    ]
    df1, results1 = task_func(data, random_seed=42)
    df2, results2 = task_func(data, random_seed=42)
    
    # Check if the DataFrames are identical
    pd.testing.assert_frame_equal(df1, df2)
    
    # Check if the regression results are identical
    assert results1.params.equals(results2.params)
    assert results1.rsquared == results2.rsquared
    assert results1.fvalue == results2.fvalue