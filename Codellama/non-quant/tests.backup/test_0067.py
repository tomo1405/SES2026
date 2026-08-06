import pytest
from src_0067 import task_func
import pandas as pd
import seaborn as sns

def test_task_func():
    data = [
        {'col1': 'A', 'col2': 'B', 'col3': 'C'},
        {'col1': 'A', 'col2': 'B', 'col3': 'D'},
        {'col1': 'A', 'col2': 'C', 'col3': 'D'},
        {'col1': 'B', 'col2': 'C', 'col3': 'D'},
        {'col1': 'B', 'col2': 'C', 'col3': 'E'},
        {'col1': 'B', 'col2': 'D', 'col3': 'E'},
        {'col1': 'C', 'col2': 'D', 'col3': 'E'},
        {'col1': 'C', 'col2': 'D', 'col3': 'F'},
        {'col1': 'C', 'col2': 'E', 'col3': 'F'},
        {'col1': 'D', 'col2': 'E', 'col3': 'F'},
    ]
    expected_analyzed_df = pd.DataFrame(
        {'col1': ['A', 'B', 'C', 'D'],
         'col2': ['B', 'C', 'D', 'E'],
         'col3': [2, 3, 2, 1]
        })
    expected_ax = sns.distplot(expected_analyzed_df['col3'])

    analyzed_df, ax = task_func(data)

    assert analyzed_df.equals(expected_analyzed_df)
    assert ax.equals(expected_ax)