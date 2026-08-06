import pytest
from src_0048 import task_func
import pandas as pd
import numpy as np
import io
import matplotlib.pyplot as plt

@pytest.fixture
def sample_df():
    data = {
        'A': [1, 2, np.nan, 4],
        'B': [5, np.nan, 7, 8],
        'C': [9, 10, 11, 12]
    }
    return pd.DataFrame(data)

def test_task_func(sample_df):
    df, heatmap = task_func(sample_df)
    
    # Check if NaN values are filled with mean
    assert df.isnull().sum().sum() == 0
    
    # Check if the DataFrame is standardized
    assert np.allclose(df.mean(), 0)
    assert np.allclose(df.std(), 1)
    
    # Check if the heatmap is a matplotlib Axes object
    assert isinstance(heatmap, plt.Axes)

def test_task_func_with_no_nan(sample_df):
    df = sample_df.dropna()
    df, heatmap = task_func(df)
    
    # Check if NaN values are filled with mean (no change expected in this case)
    assert df.isnull().sum().sum() == 0
    
    # Check if the DataFrame is standardized
    assert np.allclose(df.mean(), 0)
    assert np.allclose(df.std(), 1)
    
    # Check if the heatmap is a matplotlib Axes object
    assert isinstance(heatmap, plt.Axes)

def test_task_func_with_empty_df():
    df = pd.DataFrame()
    with pytest.raises(ValueError) as excinfo:
        task_func(df)
    assert "No data is present in the DataFrame" in str(excinfo.value)