import pandas as pd
import seaborn as sns
from src_0609 import task_func


def test_task_func():
    # Test case 1: df is not empty, tuples is not empty, n_plots is greater than 0
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
    tuples = [(1, 4), (2, 5)]
    n_plots = 2
    expected_df = pd.DataFrame({'A': [3], 'B': [6], 'C': [9]})
    expected_plots = [sns.Pairplot(df, vars=['A', 'B']), sns.Pairplot(df, vars=['B', 'C'])]
    actual_df, actual_plots = task_func(df, tuples, n_plots)
    assert actual_df.equals(expected_df)
    assert actual_plots == expected_plots

    # Test case 2: df is not empty, tuples is empty, n_plots is 0
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
    tuples = []
    n_plots = 0
    expected_df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
    expected_plots = []
    actual_df, actual_plots = task_func(df, tuples, n_plots)
    assert actual_df.equals(expected_df)
    assert actual_plots == expected_plots

    # Test case 3: df is empty, tuples is not empty, n_plots is greater than 0
    df = pd.DataFrame()
    tuples = [(1, 4), (2, 5)]
    n_plots = 2
    expected_df = pd.DataFrame()
    expected_plots = []
    actual_df, actual_plots = task_func(df, tuples, n_plots)
    assert actual_df.equals(expected_df)
    assert actual_plots == expected_plots