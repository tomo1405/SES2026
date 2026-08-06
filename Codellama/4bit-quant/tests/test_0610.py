import pandas as pd
from src_0610 import task_func


def test_task_func():
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9], 'D': [10, 11, 12], 'E': [13, 14, 15]})
    tuples = [('A', 'B'), ('C', 'D')]
    n_plots = 2
    expected_df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9], 'D': [10, 11, 12], 'E': [13, 14, 15]})
    expected_plots = [('A', 'B'), ('C', 'D')]
    actual_df, actual_plots = task_func(df, tuples, n_plots)
    assert actual_df.equals(expected_df)
    assert actual_plots == expected_plots