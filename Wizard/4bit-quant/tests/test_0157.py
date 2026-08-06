python
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
    data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9], 'D': [10, 11, 12], 'E': [13, 14, 15], 'F': [16, 17, 18], 'G': [19, 20, 21], 'H': [22, 23, 24]})
    df, ax = task_func(data)

    assert df.shape == (3, 9)
    assert df.columns.tolist() == ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'Average']
    assert df['Average'].tolist() == [10.0, 13.5, 17.0]
    assert ax.get_xlabel() == 'Index'
    assert ax.get_ylabel() == 'Average'
    assert ax.get_title() == 'Average'