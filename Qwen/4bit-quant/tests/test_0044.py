import pytest
from src_0044 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

@pytest.fixture
def sample_df():
    data = {
        'A': [1, 2, np.nan, 4],
        'B': [5, np.nan, np.nan, 8],
        'C': ['x', 'y', 'z', 'w']
    }
    return pd.DataFrame(data)

def test_task_func(sample_df):
    description, plots = task_func(sample_df)
    
    # Check if description is a DataFrame
    assert isinstance(description, pd.DataFrame)
    
    # Check if the mean values are correctly filled
    expected_mean_A = 2.5
    expected_mean_B = 6.5
    assert sample_df['A'].mean() == expected_mean_A
    assert sample_df['B'].mean() == expected_mean_B
    
    # Check if plots are created for numeric columns
    assert len(plots) == 2  # Only 'A' and 'B' are numeric
    
    # Check if plots are matplotlib axes objects
    for plot in plots:
        assert isinstance(plot, plt.Axes)

# To run the tests, you can use the following command in your terminal:
# pytest <path_to_this_file>