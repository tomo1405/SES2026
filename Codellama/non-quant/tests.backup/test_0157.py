import pytest
from src_0157 import task_func
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

def test_task_func():
    data = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [6, 7, 8, 9, 10], 'C': [11, 12, 13, 14, 15], 'D': [16, 17, 18, 19, 20], 'E': [21, 22, 23, 24, 25], 'F': [26, 27, 28, 29, 30], 'G': [31, 32, 33, 34, 35], 'H': [36, 37, 38, 39, 40]})
    expected_df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [6, 7, 8, 9, 10], 'C': [11, 12, 13, 14, 15], 'D': [16, 17, 18, 19, 20], 'E': [21, 22, 23, 24, 25], 'F': [26, 27, 28, 29, 30], 'G': [31, 32, 33, 34, 35], 'H': [36, 37, 38, 39, 40], 'Average': [15.5, 16.5, 17.5, 18.5, 19.5]})
    expected_ax = plt.subplots()
    expected_ax.plot(expected_df['Average'])

    df, ax = task_func(data)

    assert df.equals(expected_df)
    assert ax.get_xlabel() == 'Average'
    assert ax.get_ylabel() == 'Average'
    assert ax.get_title() == 'Average'
    assert ax.get_xlim() == (0, 5)
    assert ax.get_ylim() == (0, 100)
    assert ax.get_xticks() == [0, 1, 2, 3, 4, 5]
    assert ax.get_yticks() == [0, 25, 50, 75, 100]
    assert ax.get_xticklabels() == ['0', '1', '2', '3', '4', '5']
    assert ax.get_yticklabels() == ['0', '25', '50', '75', '100']