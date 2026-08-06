import pytest
from src_0612 import task_func

def test_task_func():
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [6, 7, 8, 9, 10], 'C': [11, 12, 13, 14, 15], 'D': [16, 17, 18, 19, 20], 'E': [21, 22, 23, 24, 25]})
    tuples = [(1, 2), (3, 4), (5, 6)]
    n_plots = 3

    df_result, plot_details = task_func(df, tuples, n_plots)

    assert df_result.shape == (5, 5)
    assert len(plot_details) == 3
    assert all(plot_detail in COLUMNS for plot_detail in plot_details)