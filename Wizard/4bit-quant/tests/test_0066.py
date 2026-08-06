python
import pandas as pd
import matplotlib.pyplot as plt
import pytest

COLUMNS = ['col1', 'col2', 'col3']

def task_func(data):
    df = pd.DataFrame(data, columns=COLUMNS)
    analyzed_df = df.groupby(COLUMNS[:-1])[COLUMNS[-1]].nunique().reset_index()

    # Adjusting the plotting logic
    fig, ax = plt.subplots()
    ax.plot(analyzed_df[COLUMNS[:-1]].astype(str).agg('-'.join, axis=1), analyzed_df[COLUMNS[-1]])
    ax.set_xlabel('-'.join(COLUMNS[:-1]))
    ax.set_ylabel(COLUMNS[-1])

    return analyzed_df, ax

def test_task_func():
    data = [
        {'col1': 'A', 'col2': 'B', 'col3': 1},
        {'col1': 'A', 'col2': 'C', 'col3': 2},
        {'col1': 'B', 'col2': 'C', 'col3': 3},
        {'col1': 'B', 'col2': 'D', 'col3': 4},
        {'col1': 'C', 'col2': 'D', 'col3': 5},
        {'col1': 'C', 'col2': 'E', 'col3': 6},
    ]

    analyzed_df, ax = task_func(data)

    assert analyzed_df.shape == (3, 3)
    assert list(analyzed_df.columns) == ['col1', 'col2', 'col3']
    assert list(analyzed_df['col1'].unique()) == ['A', 'B', 'C']
    assert list(analyzed_df['col2'].unique()) == ['B', 'C', 'D', 'E']
    assert list(analyzed_df['col3'].unique()) == [1, 2, 3, 4, 5, 6]

    assert ax.get_xlabel() == 'col1-col2'
    assert ax.get_ylabel() == 'col3'