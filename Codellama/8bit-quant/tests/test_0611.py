import pytest
from src_0611 import task_func
import pandas as pd
import seaborn as sns


def test_task_func_empty_df():
    df = pd.DataFrame()
    tuples = [(1, 2, 3, 4, 5)]
    n_plots = 2
    expected_df = pd.DataFrame()
    expected_plots = []
    actual_df, actual_plots = task_func(df, tuples, n_plots)
    assert actual_df.equals(expected_df)
    assert actual_plots == expected_plots


def test_task_func_non_empty_df():
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [6, 7, 8, 9, 10], 'C': [11, 12, 13, 14, 15], 'D': [16, 17, 18, 19, 20], 'E': [21, 22, 23, 24, 25]})
    tuples = [(1, 2, 3, 4, 5)]
    n_plots = 2
    expected_df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [6, 7, 8, 9, 10], 'C': [11, 12, 13, 14, 15], 'D': [16, 17, 18, 19, 20], 'E': [21, 22, 23, 24, 25]})
    expected_plots = [sns.jointplot(data=df, x='A', y='B'), sns.jointplot(data=df, x='C', y='D')]
    actual_df, actual_plots = task_func(df, tuples, n_plots)
    assert actual_df.equals(expected_df)
    assert actual_plots == expected_plots


def test_task_func_non_empty_df_with_no_tuples():
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [6, 7, 8, 9, 10], 'C': [11, 12, 13, 14, 15], 'D': [16, 17, 18, 19, 20], 'E': [21, 22, 23, 24, 25]})
    tuples = []
    n_plots = 2
    expected_df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [6, 7, 8, 9, 10], 'C': [11, 12, 13, 14, 15], 'D': [16, 17, 18, 19, 20], 'E': [21, 22, 23, 24, 25]})
    expected_plots = [sns.jointplot(data=df, x='A', y='B'), sns.jointplot(data=df, x='C', y='D')]
    actual_df, actual_plots = task_func(df, tuples, n_plots)
    assert actual_df.equals(expected_df)
    assert actual_plots == expected_plots