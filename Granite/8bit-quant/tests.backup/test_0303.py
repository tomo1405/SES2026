import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from src_0303 import task_func
import pytest

# Constants
COLUMNS = ['Date', 'Value']

# Test 1: Check if the function raises a ValueError when the input DataFrame is invalid
def test_task_func_invalid_df():
    invalid_df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    with pytest.raises(ValueError):
        task_func(invalid_df)

# Test 2: Check if the function returns the correlation DataFrame when plot=False
def test_task_func_no_plot():
    valid_df = pd.DataFrame({
        'Date': ['2022-01-01', '2022-01-02', '2022-01-03'],
        'Value': [10, 20, 30]
    })
    corr_df = task_func(valid_df)
    assert isinstance(corr_df, pd.DataFrame)

# Test 3: Check if the function returns both the correlation DataFrame and the heatmap object when plot=True
def test_task_func_with_plot():
    valid_df = pd.DataFrame({
        'Date': ['2022-01-01', '2022-01-02', '2022-01-03'],
        'Value': [10, 20, 30]
    })
    corr_df, heatmap = task_func(valid_df, plot=True)
    assert isinstance(corr_df, pd.DataFrame)
    assert isinstance(heatmap, plt.Axes)