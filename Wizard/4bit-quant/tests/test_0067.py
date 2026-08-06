python
import pandas as pd
import seaborn as sns
import pytest

# Constants
COLUMNS = ['col1', 'col2', 'col3']

def task_func(data):
    df = pd.DataFrame(data, columns=COLUMNS)
    analyzed_df = df.groupby(COLUMNS[:-1])[COLUMNS[-1]].nunique().reset_index()
    ax = sns.distplot(analyzed_df[COLUMNS[-1]])

    return analyzed_df, ax

def test_task_func():
    # Test case 1
    data = [
        ['A', 1, 2, 3],
        ['B', 2, 3, 4],
        ['C', 3, 4, 5],
        ['A', 4, 5, 6],
        ['B', 5, 6, 7],
        ['C', 6, 7, 8]
    ]
    expected_analyzed_df = pd.DataFrame([
        ['A', 2],
        ['B', 2],
        ['C', 2]
    ], columns=COLUMNS[:-1] + [COLUMNS[-1]])
    expected_ax = None
    analyzed_df, ax = task_func(data)
    assert analyzed_df.equals(expected_analyzed_df)
    assert ax == expected_ax

    # Test case 2
    data = [
        ['A', 1, 2, 3],
        ['B', 2, 3, 4],
        ['C', 3, 4, 5],
        ['A', 4, 5, 6],
        ['B', 5, 6, 7],
        ['C', 6, 7, 8],
        ['A', 7, 8, 9],
        ['B', 8, 9, 10],
        ['C', 9, 10, 11]
    ]
    expected_analyzed_df = pd.DataFrame([
        ['A', 3],
        ['B', 3],
        ['C', 3]
    ], columns=COLUMNS[:-1] + [COLUMNS[-1]])
    expected_ax = None
    analyzed_df, ax = task_func(data)
    assert analyzed_df.equals(expected_analyzed_df)
    assert ax == expected_ax