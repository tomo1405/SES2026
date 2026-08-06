import pytest
from src_0134 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def test_task_func_invalid_input():
    with pytest.raises(ValueError, match="Input must be a non-empty DataFrame."):
        task_func(None)
    with pytest.raises(ValueError, match="Input must be a non-empty DataFrame."):
        task_func(pd.DataFrame())

def test_task_func_valid_input():
    data = {
        'A': [1, 2, 3, 4, 5],
        'B': [5, 4, 3, 2, 1]
    }
    df = pd.DataFrame(data)
    normalized_df, ax = task_func(df)
    
    # Check if the output is a DataFrame
    assert isinstance(normalized_df, pd.DataFrame)
    
    # Check if the last column is normalized
    last_col = normalized_df.columns[-1]
    assert np.all(normalized_df[last_col] >= 0) and np.all(normalized_df[last_col] <= 1)
    
    # Check if the plot is created
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == 'Normalized Data of B'
    assert ax.get_xlabel() == 'Index'
    assert ax.get_ylabel() == 'Normalized Value'

def test_task_func_single_column():
    data = {'A': [1, 2, 3, 4, 5]}
    df = pd.DataFrame(data)
    normalized_df, ax = task_func(df)
    
    # Check if the output is a DataFrame
    assert isinstance(normalized_df, pd.DataFrame)
    
    # Check if the last column is normalized
    last_col = normalized_df.columns[-1]
    assert np.all(normalized_df[last_col] >= 0) and np.all(normalized_df[last_col] <= 1)
    
    # Check if the plot is created
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == 'Normalized Data of A'
    assert ax.get_xlabel() == 'Index'
    assert ax.get_ylabel() == 'Normalized Value'