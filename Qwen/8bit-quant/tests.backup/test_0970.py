import pytest
from src_0970 import task_func
import pandas as pd
import numpy as np

def test_task_func_numeric_data():
    # Test with numeric data
    df = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    })
    result = task_func(df)
    assert isinstance(result, pd.DataFrame)
    assert result.shape == df.shape
    assert (result.columns == df.columns).all()

def test_task_func_non_numeric_data():
    # Test with non-numeric data
    df = pd.DataFrame({
        'A': [1, 2, 3],
        'B': ['a', 'b', 'c']
    })
    with pytest.raises(TypeError, match="Input DataFrame contains non-numeric data types."):
        task_func(df)

def test_task_func_empty_dataframe():
    # Test with empty DataFrame
    df = pd.DataFrame()
    with pytest.raises(ValueError, match="Input DataFrame is empty or contains NaN values."):
        task_func(df)

def test_task_func_dataframe_with_nan():
    # Test with DataFrame containing NaN values
    df = pd.DataFrame({
        'A': [1, 2, np.nan],
        'B': [4, 5, 6]
    })
    with pytest.raises(ValueError, match="Input DataFrame is empty or contains NaN values."):
        task_func(df)

def test_task_func_single_column():
    # Test with a single column DataFrame
    df = pd.DataFrame({
        'A': [1, 2, 3]
    })
    result = task_func(df)
    assert isinstance(result, pd.DataFrame)
    assert result.shape == df.shape
    assert (result.columns == df.columns).all()

def test_task_func_all_zeros():
    # Test with all zeros DataFrame
    df = pd.DataFrame({
        'A': [0, 0, 0],
        'B': [0, 0, 0]
    })
    result = task_func(df)
    assert isinstance(result, pd.DataFrame)
    assert result.shape == df.shape
    assert (result.columns == df.columns).all()
    assert (result == 0).all().all()

def test_task_func_negative_values():
    # Test with negative values
    df = pd.DataFrame({
        'A': [-1, -2, -3],
        'B': [-4, -5, -6]
    })
    result = task_func(df)
    assert isinstance(result, pd.DataFrame)
    assert result.shape == df.shape
    assert (result.columns == df.columns).all()