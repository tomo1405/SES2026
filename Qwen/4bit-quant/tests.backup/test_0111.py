import pytest
from src_0111 import task_func
import pandas as pd

def test_task_func_with_valid_data():
    # Create a sample DataFrame with 'Date' and 'Sales' columns
    data = {
        'Date': ['2023-01-01', '2023-01-02', '2023-01-04'],
        'Sales': [100, 200, 300]
    }
    df = pd.DataFrame(data)

    # Call the function and check if it returns an Axes object
    ax = task_func(df)
    assert isinstance(ax, plt.Axes)

def test_task_func_with_invalid_dataframe_type():
    # Test with a non-DataFrame input
    with pytest.raises(ValueError, match="Invalid 'df': must be a DataFrame with 'Date' and 'Sales' columns."):
        task_func([1, 2, 3])

def test_task_func_missing_columns():
    # Test with a DataFrame missing 'Sales' column
    data = {
        'Date': ['2023-01-01', '2023-01-02']
    }
    df = pd.DataFrame(data)

    with pytest.raises(ValueError, match="Invalid 'df': must be a DataFrame with 'Date' and 'Sales' columns."):
        task_func(df)

def test_task_func_empty_after_resampling():
    # Test with a DataFrame that results in an empty DataFrame after resampling
    data = {
        'Date': ['2023-01-01'],
        'Sales': [0]
    }
    df = pd.DataFrame(data)

    with pytest.raises(ValueError, match="No data available to plot after resampling."):
        task_func(df)