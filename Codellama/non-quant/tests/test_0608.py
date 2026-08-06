import pytest
from src_0608 import task_func
import pandas as pd
import matplotlib.pyplot as plt

def test_task_func():
    # Test case 1: Ensure tuple elements match DataFrame columns for removal
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [6, 7, 8, 9, 10], 'C': [11, 12, 13, 14, 15], 'D': [16, 17, 18, 19, 20], 'E': [21, 22, 23, 24, 25]})
    tuples = [(1, 2), (3, 4), (5, 6)]
    n_plots = 2
    expected_df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [6, 7, 8, 9, 10], 'C': [11, 12, 13, 14, 15], 'D': [16, 17, 18, 19, 20], 'E': [21, 22, 23, 24, 25]})
    expected_plots = [plt.scatter(x='A', y='B', data=expected_df), plt.scatter(x='C', y='D', data=expected_df)]
    actual_df, actual_plots = task_func(df, tuples, n_plots)
    assert actual_df.equals(expected_df)
    assert len(actual_plots) == len(expected_plots)
    for actual_plot, expected_plot in zip(actual_plots, expected_plots):
        assert actual_plot.get_xlabel() == expected_plot.get_xlabel()
        assert actual_plot.get_ylabel() == expected_plot.get_ylabel()
        assert actual_plot.get_title() == expected_plot.get_title()
        assert actual_plot.get_data() == expected_plot.get_data()

    # Test case 2: Ensure random plots are generated
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [6, 7, 8, 9, 10], 'C': [11, 12, 13, 14, 15], 'D': [16, 17, 18, 19, 20], 'E': [21, 22, 23, 24, 25]})
    tuples = [(1, 2), (3, 4), (5, 6)]
    n_plots = 2
    expected_df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [6, 7, 8, 9, 10], 'C': [11, 12, 13, 14, 15], 'D': [16, 17, 18, 19, 20], 'E': [21, 22, 23, 24, 25]})
    expected_plots = [plt.scatter(x='A', y='B', data=expected_df), plt.scatter(x='C', y='D', data=expected_df)]
    actual_df, actual_plots = task_func(df, tuples, n_plots)
    assert actual_df.equals(expected_df)
    assert len(actual_plots) == len(expected_plots)
    for actual_plot, expected_plot in zip(actual_plots, expected_plots):
        assert actual_plot.get_xlabel() == expected_plot.get_xlabel()
        assert actual_plot.get_ylabel() == expected_plot.get_ylabel()
        assert actual_plot.get_title() == expected_plot.get_title()
        assert actual_plot.get_data() == expected_plot.get_data()

    # Test case 3: Ensure correct number of plots are generated
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [6, 7, 8, 9, 10], 'C': [11, 12, 13, 14, 15], 'D': [16, 17, 18, 19, 20], 'E': [21, 22, 23, 24, 25]})
    tuples = [(1, 2), (3, 4), (5, 6)]
    n_plots = 3
    expected_df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [6, 7, 8, 9, 10], 'C': [11, 12, 13, 14, 15], 'D': [16, 17, 18, 19, 20], 'E': [21, 22, 23, 24, 25]})
    expected_plots = [plt.scatter(x='A', y='B', data=expected_df), plt.scatter(x='C', y='D', data=expected_df), plt.scatter(x='E', y='A', data=expected_df)]
    actual_df, actual_plots = task_func(df, tuples, n_plots)
    assert actual_df.equals(expected_df)
    assert len(actual_plots) == len(expected_plots)
    for actual_plot, expected_plot in zip(actual_plots, expected_plots):
        assert actual_plot.get_xlabel() == expected_plot.get_xlabel()
        assert actual_plot.get_ylabel() == expected_plot.get_ylabel()
        assert actual_plot.get_title() == expected_plot.get_title()
        assert actual_plot.get_data() == expected_plot.get_data()