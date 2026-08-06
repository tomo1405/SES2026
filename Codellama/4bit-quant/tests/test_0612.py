import pandas as pd
from src_0612 import task_func


def test_task_func():
    # Test case 1: n_plots is less than the number of rows in the dataframe
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
    tuples = [('A', 'B'), ('C', 'D')]
    n_plots = 2
    expected_df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
    expected_plot_details = [('A', 'B'), ('C', 'D')]
    actual_df, actual_plot_details = task_func(df, tuples, n_plots)
    assert actual_df.equals(expected_df)
    assert actual_plot_details == expected_plot_details

    # Test case 2: n_plots is greater than the number of rows in the dataframe
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
    tuples = [('A', 'B'), ('C', 'D')]
    n_plots = 4
    expected_df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
    expected_plot_details = [('A', 'B'), ('C', 'D')]
    actual_df, actual_plot_details = task_func(df, tuples, n_plots)
    assert actual_df.equals(expected_df)
    assert actual_plot_details == expected_plot_details

    # Test case 3: tuples is empty
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
    tuples = []
    n_plots = 2
    expected_df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
    expected_plot_details = []
    actual_df, actual_plot_details = task_func(df, tuples, n_plots)
    assert actual_df.equals(expected_df)
    assert actual_plot_details == expected_plot_details

    # Test case 4: tuples is not a list of tuples
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
    tuples = 'A,B'
    n_plots = 2
    expected_df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
    expected_plot_details = []
    actual_df, actual_plot_details = task_func(df, tuples, n_plots)
    assert actual_df.equals(expected_df)
    assert actual_plot_details == expected_plot_details

    # Test case 5: n_plots is not an integer
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
    tuples = [('A', 'B'), ('C', 'D')]
    n_plots = 2.5
    expected_df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
    expected_plot_details = []
    actual_df, actual_plot_details = task_func(df, tuples, n_plots)
    assert actual_df.equals(expected_df)
    assert actual_plot_details == expected_plot_details