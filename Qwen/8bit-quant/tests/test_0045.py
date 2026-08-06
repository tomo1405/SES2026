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
    df_result, ax = task_func(sample_df)
    
    # Check if the DataFrame has been filled with mean values
    assert df_result.isnull().sum().sum() == 0
    
    # Check if the DataFrame has been scaled between 0 and 1
    assert df_result.min().min() >= 0
    assert df_result.max().max() <= 1
    
    # Check if the boxplot was created
    assert isinstance(ax, plt.Axes)
    
    # Check if the figure size is correct
    assert ax.get_figure().get_size_inches() == (10, 5)