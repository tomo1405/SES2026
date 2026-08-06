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
        'C': ['x', 'y', 'z', 'w']
    }
    return pd.DataFrame(data)

def test_task_func(sample_df):
    description, plots = task_func(sample_df)
    
    # Check if description is a DataFrame
    assert isinstance(description, pd.DataFrame)
    
    # Check if description contains expected columns
    expected_columns = ['count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max']
    assert all(col in description.columns for col in expected_columns)
    
    # Check if plots is a list
    assert isinstance(plots, list)
    
    # Check if each plot is a matplotlib Axes object
    for plot in plots:
        assert isinstance(plot, plt.Axes)
    
    # Check if the number of plots matches the number of numeric columns
    numeric_columns = sample_df.select_dtypes(include=[np.number]).columns
    assert len(plots) == len(numeric_columns)
    
    # Check if NaN values have been filled with the mean
    filled_df = sample_df.fillna(sample_df.mean(axis=0))
    assert filled_df.equals(sample_df.drop(columns='C'))

# Run the tests
if __name__ == "__main__":
    pytest.main()