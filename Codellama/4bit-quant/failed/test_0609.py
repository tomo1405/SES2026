import pytest
from src_0609 import task_func

def test_task_func():
    # Test case 1: Empty dataframe
    df = pd.DataFrame()
    tuples = []
    n_plots = 0
    expected_df = pd.DataFrame()
    expected_plots = []
    assert task_func(df, tuples, n_plots) == (expected_df, expected_plots)

    # Test case 2: Non-empty dataframe, no tuples, no plots
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
    tuples = []
    n_plots = 0
    expected_df = df
    expected_plots = []
    assert task_func(df, tuples, n_plots) == (expected_df, expected_plots)

    # Test case 3: Non-empty dataframe, no tuples, 1 plot
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
    tuples = []
    n_plots = 1
    expected_df = df
    expected_plots = [sns.pairplot(df, vars=['A', 'B'])]
    assert task_func(df, tuples, n_plots) == (expected_df, expected_plots)

    # Test case 4: Non-empty dataframe, no tuples, 2 plots
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
    tuples = []
    n_plots = 2
    expected_df = df
    expected_plots = [sns.pairplot(df, vars=['A', 'B']), sns.pairplot(df, vars=['C', 'A'])]
    assert task_func(df, tuples, n_plots) == (expected_df, expected_plots)

    # Test case 5: Non-empty dataframe, tuples, no plots
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
    tuples = [(1, 2), (3, 4)]
    n_plots = 0
    expected_df = df[~df.apply(tuple, axis=1).isin(tuples)]
    expected_plots = []
    assert task_func(df, tuples, n_plots) == (expected_df, expected_plots)

    # Test case 6: Non-empty dataframe, tuples, 1 plot
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
    tuples = [(1, 2), (3, 4)]
    n_plots = 1
    expected_df = df[~df.apply(tuple, axis=1).isin(tuples)]
    expected_plots = [sns.pairplot(df, vars=['A', 'B'])]
    assert task_func(df, tuples, n_plots) == (expected_df, expected_plots)

    # Test case 7: Non-empty dataframe, tuples, 2 plots
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
    tuples = [(1, 2), (3, 4)]
    n_plots = 2
    expected_df = df[~df.apply(tuple, axis=1).isin(tuples)]
    expected_plots = [sns.pairplot(df, vars=['A', 'B']), sns.pairplot(df, vars=['C', 'A'])]
    assert task_func(df, tuples, n_plots) == (expected_df, expected_plots)