import pytest
from src_0045 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

@pytest.fixture
def sample_df():
    data = {
        'A': [1, 2, np.nan, 4],
        'B': [5, np.nan, np.nan, 8],
        'C': [9, 10, 11, 12]
    }
    return pd.DataFrame(data)

def test_task_func(sample_df):
    df, ax = task_func(sample_df)
    
    # Check if NaN values are filled with mean
    assert df.isnull().values.any() == False, "NaN values should be filled"
    
    # Check if scaling is applied correctly
    assert df.min().min() >= 0, "Minimum value after scaling should be >= 0"
    assert df.max().max() <= 1, "Maximum value after scaling should be <= 1"
    
    # Check if boxplot is created
    assert isinstance(ax, plt.Axes), "Function should return a matplotlib Axes object"

def test_task_func_with_no_nan(sample_df):
    # Fill all NaN values before passing to the function
    sample_df_filled = sample_df.fillna(sample_df.mean())
    df, ax = task_func(sample_df_filled)
    
    # Check if scaling is applied correctly
    assert df.min().min() >= 0, "Minimum value after scaling should be >= 0"
    assert df.max().max() <= 1, "Maximum value after scaling should be <= 1"
    
    # Check if boxplot is created
    assert isinstance(ax, plt.Axes), "Function should return a matplotlib Axes object"

def test_task_func_with_empty_df():
    empty_df = pd.DataFrame()
    with pytest.raises(ValueError):
        task_func(empty_df)