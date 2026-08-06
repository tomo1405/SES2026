import pandas as pd
from src_0612 import task_func


def test_task_func():
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [2, 4, 6, 8, 10], 'C': [3, 6, 9, 12, 15], 'D': [4, 8, 12, 16, 20], 'E': [5, 10, 15, 20, 25]})
    tuples = [(1, 2), (3, 4), (5, 6)]
    n_plots = 3

    df_out, plot_details = task_func(df, tuples, n_plots)

    assert df_out.shape == (3, 5)
    assert len(plot_details) == 3
    assert all(plot_detail in COLUMNS for plot_detail in plot_details)
    assert all(plot_detail in COLUMNS for plot_detail in plot_details)
    assert all(plot_detail in COLUMNS for plot_detail in plot_details)