python
import pandas as pd
import matplotlib.pyplot as plt
from random import sample
from src_0608 import task_func

# Constants for column names to use in plots
COLUMNS = ['A', 'B', 'C', 'D', 'E']

# Test case 1: Test with valid input
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9], 'D': [10, 11, 12], 'E': [13, 14, 15]})
tuples = [('A', 'B'), ('C', 'D')]
n_plots = 2
expected_df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9], 'D': [10, 11, 12], 'E': [13, 14, 15]})
expected_plots = []
for _ in range(n_plots):
    selected_columns = sample(COLUMNS, 2)
    ax = expected_df.plot(x=selected_columns[0], y=selected_columns[1], kind='scatter')
    expected_plots.append(ax)

def test_task_func():
    actual_df, actual_plots = task_func(df, tuples, n_plots)
    assert actual_df.equals(expected_df)
    assert len(actual_plots) == len(expected_plots)
    for i in range(len(actual_plots)):
        assert actual_plots[i] == expected_plots[i]

# Test case 2: Test with invalid input
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9], 'D': [10, 11, 12], 'E': [13, 14, 15]})
tuples = [('A', 'B'), ('C', 'D')]
n_plots = 2
expected_df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9], 'D': [10, 11, 12], 'E': [13, 14, 15]})
expected_plots = []
for _ in range(n_plots):
    selected_columns = sample(COLUMNS, 2)
    ax = expected_df.plot(x=selected_columns[0], y=selected_columns[1], kind='scatter')
    expected_plots.append(ax)

def test_task_func_invalid_input():
    actual_df, actual_plots = task_func(df, tuples, n_plots)
    assert actual_df.equals(expected_df)
    assert len(actual_plots) == len(expected_plots)
    for i in range(len(actual_plots)):
        assert actual_plots[i] == expected_plots[i]