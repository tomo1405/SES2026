import pytest
from src_0106 import task_func
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Mocking functions to avoid actual plotting
def mock_savefig(self, *args, **kwargs):
    pass

plt.Figure.savefig = mock_savefig

def test_task_func_valid_input():
    # Create a sample DataFrame
    data = {
        'group': ['A', 'B', 'A', 'B'],
        'date': pd.date_range(start='2023-01-01', periods=4),
        'value': [10, 20, 30, 40]
    }
    df = pd.DataFrame(data)
    
    # Call the function
    heatmap_fig, pairplot_grid = task_func(df)
    
    # Check that the outputs are of the correct type
    assert isinstance(heatmap_fig, plt.Figure)
    assert isinstance(pairplot_grid, sns.axisgrid.PairGrid)

def test_task_func_empty_df():
    df = pd.DataFrame()
    
    with pytest.raises(ValueError) as excinfo:
        task_func(df)
    
    assert str(excinfo.value) == "DataFrame must be non-empty and contain 'group', 'date', and 'value' columns."

def test_task_func_missing_columns():
    data = {
        'group': ['A', 'B', 'A', 'B'],
        'date': pd.date_range(start='2023-01-01', periods=4)
    }
    df = pd.DataFrame(data)
    
    with pytest.raises(ValueError) as excinfo:
        task_func(df)
    
    assert str(excinfo.value) == "DataFrame must be non-empty and contain 'group', 'date', and 'value' columns."

def test_task_func_non_datetime_date_column():
    data = {
        'group': ['A', 'B', 'A', 'B'],
        'date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04'],
        'value': [10, 20, 30, 40]
    }
    df = pd.DataFrame(data)
    
    with pytest.raises(ValueError) as excinfo:
        task_func(df)
    
    assert str(excinfo.value) == "'date' column must be in datetime format."