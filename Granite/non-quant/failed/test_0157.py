import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import pytest

def task_func(data):
    COLUMN_NAMES = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    scaler = MinMaxScaler()
    normalized_data = scaler.fit_transform(data)

    df = pd.DataFrame(normalized_data, columns=COLUMN_NAMES)
    df['Average'] = df.mean(axis=1)

    fig, ax = plt.subplots()
    df['Average'].plot(ax=ax)

    return df, ax

def test_task_func():
    data = [[1, 2, 3, 4, 5, 6, 7, 8], [9, 10, 11, 12, 13, 14, 15, 16]]
    df, ax = task_func(data)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert list(df.columns) == ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'Average']
    assert ax.get_xlabel() == 'Index'
    assert ax.get_ylabel() == 'Average'