import pytest
from src_0305 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

@pytest.fixture
def sample_df():
    data = {
        'Date': ['2021-01-01', '2021-01-02', '2021-01-03'],
        'Value': [[1, 2], [3, 4], [5, 6]]
    }
    return pd.DataFrame(data)

def test_task_func_with_empty_df():
    df = pd.DataFrame()
    result = task_func(df)
    assert result == (0, 0)

def test_task_func_with_sample_data(sample_df):
    explained_variance_ratio, ax = task_func(sample_df)
    
    # Check if explained_variance_ratio is a numpy array
    assert isinstance(explained_variance_ratio, np.ndarray)
    
    # Check if the length of explained_variance_ratio is correct
    assert len(explained_variance_ratio) == 2
    
    # Check if ax is a matplotlib Axes object
    assert isinstance(ax, plt.Axes)
    
    # Check if the plot has the correct title and labels
    assert ax.get_title() == 'Explained Variance Ratio of Principal Components'
    assert ax.get_xlabel() == 'Principal Component'
    assert ax.get_ylabel() == 'Explained Variance Ratio'

def test_task_func_with_single_value_column(sample_df):
    sample_df['Value'] = [[1], [2], [3]]
    explained_variance_ratio, ax = task_func(sample_df)
    
    # Check if explained_variance_ratio is a numpy array
    assert isinstance(explained_variance_ratio, np.ndarray)
    
    # Check if the length of explained_variance_ratio is correct
    assert len(explained_variance_ratio) == 1
    
    # Check if ax is a matplotlib Axes object
    assert isinstance(ax, plt.Axes)
    
    # Check if the plot has the correct title and labels
    assert ax.get_title() == 'Explained Variance Ratio of Principal Components'
    assert ax.get_xlabel() == 'Principal Component'
    assert ax.get_ylabel() == 'Explained Variance Ratio'