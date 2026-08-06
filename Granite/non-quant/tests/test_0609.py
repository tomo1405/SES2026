import pandas as pd
from src_0609 import task_func


def test_task_func():
    # Test case 1: df is empty
    df = pd.DataFrame()
    tuples = [(1, 2), (3, 4)]
    n_plots = 2
    expected_df = pd.DataFrame()
    expected_plots = []
    actual_df, actual_plots = task_func(df, tuples, n_plots)
    assert actual_df.equals(expected_df)
    assert actual_plots == expected_plots

    # Test case 2: df is not empty, but no tuples found
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
    tuples = [(1, 2), (3, 4)]
    n_plots = 2
    expected_df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
    expected_plots = []
    actual_df, actual_plots = task_func(df, tuples, n_plots)
    assert actual_df.equals(expected_df)
    assert actual_plots == expected_plots

    # Test case 3: df is not empty, tuples found, and n_plots > 0
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
    tuples = [(1, 4), (3, 6)]
    n_plots = 2
    expected_df = pd.DataFrame({'A': [2, 3], 'B': [5, 6], 'C': [8, 9]})
    expected_plots = []  # No plots generated in this case
    actual_df, actual_plots = task_func(df, tuples, n_plots)
    assert actual_df.equals(expected_df)
    assert actual_plots == expected_plots

    # Test case 4: df is not empty, tuples found, n_plots > 0, and enough columns for pairplot
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9], 'D': [10, 11, 12], 'E': [13, 14, 15]})
    tuples = [(1, 4), (3, 6)]
    n_plots = 3
    expected_df = pd.DataFrame({'A': [2, 3], 'B': [5, 6], 'C': [8, 9], 'D': [10, 11], 'E': [13, 14]})
    expected_plots = []  # No plots generated in this case
    actual_df, actual_plots = task_func(df, tuples, n_plots)
    assert actual_df.equals(expected_df)
    assert actual_plots == expected_plots