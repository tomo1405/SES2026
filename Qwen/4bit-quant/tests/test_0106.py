import pytest
from src_0106 import task_func
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def test_task_func_basic():
    # Create a sample DataFrame
    data = {
        'group': ['A', 'B', 'A', 'B'],
        'date': pd.date_range(start='2023-01-01', periods=4),
        'value': [10, 20, 30, 40]
    }
    df = pd.DataFrame(data)
    
    # Call the function
    heatmap_fig, pairplot_grid = task_func(df)
    
    # Check if the returned objects are of the correct type
    assert isinstance(heatmap_fig, plt.Figure)
    assert isinstance(pairplot_grid, sns.axisgrid.PairGrid)

def test_task_func_empty_df():
    # Create an empty DataFrame
    df = pd.DataFrame()
    
    # Check if the function raises a ValueError
    with pytest.raises(ValueError, match="DataFrame must be non-empty"):
        task_func(df)

def test_task_func_missing_columns():
    # Create a DataFrame missing one of the required columns
    data = {
        'group': ['A', 'B', 'A', 'B'],
        'date': pd.date_range(start='2023-01-01', periods=4)
    }
    df = pd.DataFrame(data)
    
    # Check if the function raises a ValueError
    with pytest.raises(ValueError, match="DataFrame must be non-empty and contain 'group', 'date', and 'value' columns."):
        task_func(df)

def test_task_func_non_datetime_date_column():
    # Create a DataFrame with a non-datetime 'date' column
    data = {
        'group': ['A', 'B', 'A', 'B'],
        'date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04'],
        'value': [10, 20, 30, 40]
    }
    df = pd.DataFrame(data)
    
    # Check if the function raises a ValueError
    with pytest.raises(ValueError, match="'date' column must be in datetime format."):
        task_func(df)