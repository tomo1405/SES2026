import pytest
from src_0610 import task_func
import pandas as pd
import matplotlib.pyplot as plt

@pytest.fixture
def sample_df():
    data = {
        'A': [1, 2, 3, 4],
        'B': [5, 6, 7, 8],
        'C': [9, 10, 11, 12],
        'D': [13, 14, 15, 16],
        'E': [17, 18, 19, 20]
    }
    return pd.DataFrame(data)

def test_task_func_basic(sample_df):
    tuples_to_drop = [('A', 1), ('B', 2)]
    n_plots = 3
    df, plots = task_func(sample_df, tuples_to_drop, n_plots)
    
    # Check if the DataFrame is correctly modified
    assert all(col in df.columns for col in ['A', 'B', 'C', 'D', 'E'])
    assert df.shape == (4, 5)  # No rows should be dropped in this case
    
    # Check if the number of plots is correct
    assert len(plots) == min(n_plots, 10)  # 10 possible combinations of 2 out of 5 columns
    
    # Check if each plot is a tuple with the correct structure
    for selected_columns, ax in plots:
        assert isinstance(selected_columns, tuple)
        assert len(selected_columns) == 2
        assert all(col in ['A', 'B', 'C', 'D', 'E'] for col in selected_columns)
        assert isinstance(ax, plt.Axes)

def test_task_func_no_plots(sample_df):
    tuples_to_drop = [('A', 1), ('B', 2)]
    n_plots = 0
    df, plots = task_func(sample_df, tuples_to_drop, n_plots)
    
    # Check if no plots are generated
    assert len(plots) == 0

def test_task_func_more_plots_than_possible(sample_df):
    tuples_to_drop = [('A', 1), ('B', 2)]
    n_plots = 15  # More than possible combinations
    df, plots = task_func(sample_df, tuples_to_drop, n_plots)
    
    # Check if the number of plots is limited by the possible combinations
    assert len(plots) == 10  # 10 possible combinations of 2 out of 5 columns

def test_task_func_empty_tuples(sample_df):
    tuples_to_drop = []
    n_plots = 3
    df, plots = task_func(sample_df, tuples_to_drop, n_plots)
    
    # Check if the DataFrame remains unchanged
    assert df.equals(sample_df)
    
    # Check if the number of plots is correct
    assert len(plots) == min(n_plots, 10)  # 10 possible combinations of 2 out of 5 columns