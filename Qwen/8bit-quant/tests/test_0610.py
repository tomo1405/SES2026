import matplotlib.pyplot as plt
import pandas as pd
import pytest
from src_0610 import task_func


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

def test_task_func(sample_df):
    tuples_to_drop = [(0, 1), (2, 3)]
    n_plots = 3
    df, plots = task_func(sample_df, tuples_to_drop, n_plots)
    
    # Check if the DataFrame is correctly modified
    assert all(col in df.columns for col in ['A', 'B', 'C', 'D', 'E'])
    assert df.shape == (4, 5)  # No rows should be dropped, only columns
    
    # Check if the plots list is correctly generated
    assert len(plots) == min(n_plots, len(list(combinations(['A', 'B', 'C', 'D', 'E'], 2))))
    for selected_columns, ax in plots:
        assert isinstance(ax, plt.Axes)
        assert selected_columns in list(combinations(['A', 'B', 'C', 'D', 'E'], 2))

def test_task_func_no_plots(sample_df):
    tuples_to_drop = [(0, 1), (2, 3)]
    n_plots = 0
    df, plots = task_func(sample_df, tuples_to_drop, n_plots)
    
    # Check if no plots are generated
    assert len(plots) == 0

def test_task_func_more_plots_than_possible(sample_df):
    tuples_to_drop = [(0, 1), (2, 3)]
    n_plots = 10  # More than possible combinations of 2 out of 5 columns
    df, plots = task_func(sample_df, tuples_to_drop, n_plots)
    
    # Check if the number of plots is limited by the number of possible combinations
    assert len(plots) == len(list(combinations(['A', 'B', 'C', 'D', 'E'], 2)))

def test_task_func_drop_nonexistent_tuples(sample_df):
    tuples_to_drop = [(10, 11), (12, 13)]  # Nonexistent tuples
    n_plots = 3
    df, plots = task_func(sample_df, tuples_to_drop, n_plots)
    
    # Check if the DataFrame remains unchanged
    assert df.equals(sample_df)