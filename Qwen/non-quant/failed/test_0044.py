import pytest
from src_0044 import task_func
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

@pytest.fixture
def sample_df():
    data = {
        'A': [1, 2, np.nan, 4],
        'B': [5, np.nan, np.nan, 8],
        'C': ['foo', 'bar', 'baz', 'qux']
    }
    return pd.DataFrame(data)

def test_task_func(sample_df):
    description, plots = task_func(sample_df)
    
    # Check if description is a DataFrame
    assert isinstance(description, pd.DataFrame)
    
    # Check if the mean of column 'A' is used to fill NaN values
    expected_mean_A = sample_df['A'].mean()
    filled_df = sample_df.fillna(expected_mean_A)
    assert filled_df.equals(sample_df.fillna(filled_df.mean(axis=0)))
    
    # Check if the mean of column 'B' is used to fill NaN values
    expected_mean_B = sample_df['B'].mean()
    filled_df = sample_df.fillna(expected_mean_B)
    assert filled_df.equals(sample_df.fillna(filled_df.mean(axis=0)))
    
    # Check if plots are created for numeric columns
    numeric_columns = sample_df.select_dtypes(include=[np.number]).columns
    assert len(plots) == len(numeric_columns)
    
    # Check if each plot is an Axes object
    for plot in plots:
        assert isinstance(plot, plt.Axes)
    
    # Check if the description contains the correct statistics
    expected_description = sample_df.describe()
    assert description.equals(expected_description)