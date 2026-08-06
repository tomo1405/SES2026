import pytest
from src_0981 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

@pytest.fixture
def sample_df():
    data = {
        'A': [1, 2, 3, 4, 5],
        'B': [5, 4, 3, 2, 1],
        'C': ['a', 'b', 'c', 'd', 'e']
    }
    return pd.DataFrame(data)

def test_task_func_no_numeric_columns(sample_df):
    # Remove numeric columns to simulate no numeric columns scenario
    sample_df = sample_df.drop(columns=['A', 'B'])
    with pytest.raises(ValueError, match="No numeric columns present"):
        task_func(sample_df)

def test_task_func_with_numeric_columns(sample_df):
    df, fig = task_func(sample_df)
    
    # Check if the DataFrame is returned correctly after scaling
    assert isinstance(df, pd.DataFrame)
    numeric_cols = ['A', 'B']
    for col in numeric_cols:
        assert col in df.columns
        assert df[col].dtype == np.float64
    
    # Check if the figure is returned correctly
    assert isinstance(fig, plt.Figure)
    
    # Check if the heatmap was plotted correctly
    ax = fig.axes[0]
    assert isinstance(ax, plt.Axes)
    assert len(ax.collections) > 0  # There should be at least one collection (the heatmap)

def test_task_func_scaling(sample_df):
    df, _ = task_func(sample_df)
    
    # Check if the numeric columns are scaled
    numeric_cols = ['A', 'B']
    for col in numeric_cols:
        mean = df[col].mean()
        std = df[col].std()
        assert np.isclose(mean, 0), f"Mean of {col} is not close to 0"
        assert np.isclose(std, 1), f"Standard deviation of {col} is not close to 1"