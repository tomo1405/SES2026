import pandas as pd
import seaborn as sns
from src_0609 import task_func


def test_task_func_empty_df():
    df = pd.DataFrame()
    tuples = [('A', 'B'), ('C', 'D')]
    n_plots = 2
    expected_df = pd.DataFrame()
    expected_plots = []
    actual_df, actual_plots = task_func(df, tuples, n_plots)
    assert actual_df.equals(expected_df)
    assert actual_plots == expected_plots

def test_task_func_non_empty_df():
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9], 'D': [10, 11, 12], 'E': [13, 14, 15]})
    tuples = [('A', 'B'), ('C', 'D')]
    n_plots = 2
    expected_df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9], 'D': [10, 11, 12], 'E': [13, 14, 15]})
    expected_plots = [sns.pairplot(df, vars=['A', 'B']), sns.pairplot(df, vars=['C', 'D'])]
    actual_df, actual_plots = task_func(df, tuples, n_plots)
    assert actual_df.equals(expected_df)
    assert actual_plots == expected_plots

def test_task_func_non_empty_df_with_duplicate_tuples():
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9], 'D': [10, 11, 12], 'E': [13, 14, 15]})
    tuples = [('A', 'B'), ('C', 'D'), ('A', 'B')]
    n_plots = 2
    expected_df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9], 'D': [10, 11, 12], 'E': [13, 14, 15]})
    expected_plots = [sns.pairplot(df, vars=['A', 'B']), sns.pairplot(df, vars=['C', 'D'])]
    actual_df, actual_plots = task_func(df, tuples, n_plots)
    assert actual_df.equals(expected_df)
    assert actual_plots == expected_plots

def test_task_func_non_empty_df_with_invalid_tuples():
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9], 'D': [10, 11, 12], 'E': [13, 14, 15]})
    tuples = [('A', 'B'), ('C', 'D'), ('X', 'Y')]
    n_plots = 2
    expected_df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9], 'D': [10, 11, 12], 'E': [13, 14, 15]})
    expected_plots = [sns.pairplot(df, vars=['A', 'B']), sns.pairplot(df, vars=['C', 'D'])]
    actual_df, actual_plots = task_func(df, tuples, n_plots)
    assert actual_df.equals(expected_df)
    assert actual_plots == expected_plots

def test_task_func_non_empty_df_with_invalid_n_plots():
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9], 'D': [10, 11, 12], 'E': [13, 14, 15]})
    tuples = [('A', 'B'), ('C', 'D')]
    n_plots = 0
    expected_df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9], 'D': [10, 11, 12], 'E': [13, 14, 15]})
    expected_plots = []
    actual_df, actual_plots = task_func(df, tuples, n_plots)
    assert actual_df.equals(expected_df)
    assert actual_plots == expected_plots

def test_task_func_non_empty_df_with_invalid_n_plots_2():
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9], 'D': [10, 11, 12], 'E': [13, 14, 15]})
    tuples = [('A', 'B'), ('C', 'D')]
    n_plots = 3
    expected_df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9], 'D': [10, 11, 12], 'E': [13, 14, 15]})
    expected_plots = [sns.pairplot(df, vars=['A', 'B']), sns.pairplot(df, vars=['C', 'D'])]
    actual_df, actual_plots = task_func(df, tuples, n_plots)
    assert actual_df.equals(expected_df)
    assert actual_plots == expected_plots