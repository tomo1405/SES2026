import pytest
from src_0134 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

@pytest.fixture
def sample_df():
    data = {
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    }
    return pd.DataFrame(data)

def test_task_func_with_valid_dataframe(sample_df):
    normalized_df, ax = task_func(sample_df)
    
    # Check if the returned object is a DataFrame
    assert isinstance(normalized_df, pd.DataFrame)
    
    # Check if the last column is normalized
    last_col_name = sample_df.columns[-1]
    assert all(0 <= val <= 1 for val in normalized_df[last_col_name])
    
    # Check if the plot is created correctly
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == f'Normalized Data of {last_col_name}'
    assert ax.get_xlabel() == "Index"
    assert ax.get_ylabel() == "Normalized Value"

def test_task_func_with_empty_dataframe():
    empty_df = pd.DataFrame()
    with pytest.raises(ValueError, match="Input must be a non-empty DataFrame."):
        task_func(empty_df)

def test_task_func_with_non_dataframe_input():
    with pytest.raises(ValueError, match="Input must be a non-empty DataFrame."):
        task_func([1, 2, 3])

def test_task_func_with_single_column_dataframe():
    data = {'A': [1, 2, 3]}
    single_col_df = pd.DataFrame(data)
    normalized_df, ax = task_func(single_col_df)
    
    # Check if the returned object is a DataFrame
    assert isinstance(normalized_df, pd.DataFrame)
    
    # Check if the single column is normalized
    last_col_name = single_col_df.columns[-1]
    assert all(0 <= val <= 1 for val in normalized_df[last_col_name])
    
    # Check if the plot is created correctly
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == f'Normalized Data of {last_col_name}'
    assert ax.get_xlabel() == "Index"
    assert ax.get_ylabel() == "Normalized Value"