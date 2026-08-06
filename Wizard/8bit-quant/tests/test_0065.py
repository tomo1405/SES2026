python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from src_0065 import task_func

# Constants
COLUMNS = ['col1', 'col2', 'col3']

# Test case 1
data = [
    ['A', 'X', 1],
    ['A', 'Y', 2],
    ['B', 'X', 3],
    ['B', 'Y', 4],
    ['C', 'X', 5],
    ['C', 'Y', 6],
]
expected_analyzed_df = pd.DataFrame({
    'col1': ['A', 'B', 'C'],
    'col2': ['X', 'Y', 'X', 'Y', 'X', 'Y'],
    'col3': [2, 2, 2, 2, 2, 2],
}).pivot(index='col1', columns='col2', values='col3')
expected_ax = None

def test_task_func():
    analyzed_df, ax = task_func(data)
    assert analyzed_df.equals(expected_analyzed_df)
    assert ax == expected_ax

# Test case 2
data = [
    ['A', 'X', 1],
    ['A', 'Y', 2],
    ['B', 'X', 3],
    ['B', 'Y', 4],
    ['C', 'X', 5],
    ['C', 'Y', 6],
    ['D', 'Z', 7],
]
expected_analyzed_df = pd.DataFrame({
    'col1': ['A', 'B', 'C', 'D'],
    'col2': ['X', 'Y', 'X', 'Y', 'X', 'Y', 'Z'],
    'col3': [2, 2, 2, 2, 2, 2, 1],
}).pivot(index='col1', columns='col2', values='col3')
expected_ax = None

def test_task_func_2():
    analyzed_df, ax = task_func(data)
    assert analyzed_df.equals(expected_analyzed_df)
    assert ax == expected_ax