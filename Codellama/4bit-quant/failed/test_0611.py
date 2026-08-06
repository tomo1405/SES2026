import pytest
from src_0611 import task_func

def test_task_func():
    # Test case 1: Empty DataFrame
    df = pd.DataFrame()
    tuples = []
    n_plots = 0
    expected_df = pd.DataFrame()
    expected_plots = []
    actual_df, actual_plots = task_func(df, tuples, n_plots)
    assert actual_df.equals(expected_df)
    assert actual_plots == expected_plots

    # Test case 2: Non-empty DataFrame, no tuples
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9], 'D': [10, 11, 12], 'E': [13, 14, 15]})
    tuples = []
    n_plots = 2
    expected_df = df
    expected_plots = [sns.jointplot(data=df, x='A', y='B'), sns.jointplot(data=df, x='C', y='D')]
    actual_df, actual_plots = task_func(df, tuples, n_plots)
    assert actual_df.equals(expected_df)
    assert actual_plots == expected_plots

    # Test case 3: Non-empty DataFrame, with tuples
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9], 'D': [10, 11, 12], 'E': [13, 14, 15]})
    tuples = [(0, 1), (1, 2)]
    n_plots = 2
    expected_df = df.drop(tuples, errors='ignore')
    expected_plots = [sns.jointplot(data=df, x='A', y='B'), sns.jointplot(data=df, x='C', y='D')]
    actual_df, actual_plots = task_func(df, tuples, n_plots)
    assert actual_df.equals(expected_df)
    assert actual_plots == expected_plots