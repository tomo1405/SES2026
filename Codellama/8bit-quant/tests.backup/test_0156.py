import pytest
from src_0156 import task_func
import pandas as pd
import matplotlib.pyplot as plt

# Test 1: Test that the function returns a tuple with a DataFrame and an Axes object
def test_returns_tuple():
    data = [
        [1, 2, 3, 4, 5, 6, 7, 8],
        [9, 10, 11, 12, 13, 14, 15, 16],
        [17, 18, 19, 20, 21, 22, 23, 24]
    ]
    df, ax = task_func(data)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)

# Test 2: Test that the DataFrame has the correct column names
def test_column_names():
    data = [
        [1, 2, 3, 4, 5, 6, 7, 8],
        [9, 10, 11, 12, 13, 14, 15, 16],
        [17, 18, 19, 20, 21, 22, 23, 24]
    ]
    df, ax = task_func(data)
    assert list(df.columns) == COLUMN_NAMES

# Test 3: Test that the DataFrame has the correct data
def test_data():
    data = [
        [1, 2, 3, 4, 5, 6, 7, 8],
        [9, 10, 11, 12, 13, 14, 15, 16],
        [17, 18, 19, 20, 21, 22, 23, 24]
    ]
    df, ax = task_func(data)
    assert list(df.values) == data

# Test 4: Test that the Axes object has the correct y-axis label
def test_y_axis_label():
    data = [
        [1, 2, 3, 4, 5, 6, 7, 8],
        [9, 10, 11, 12, 13, 14, 15, 16],
        [17, 18, 19, 20, 21, 22, 23, 24]
    ]
    df, ax = task_func(data)
    assert ax.get_ylabel() == 'Average'

# Test 5: Test that the Axes object has the correct x-axis label
def test_x_axis_label():
    data = [
        [1, 2, 3, 4, 5, 6, 7, 8],
        [9, 10, 11, 12, 13, 14, 15, 16],
        [17, 18, 19, 20, 21, 22, 23, 24]
    ]
    df, ax = task_func(data)
    assert ax.get_xlabel() == 'Average'