import pytest
from src_0559 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def test_task_func_empty_input():
    a = []
    b = []
    df, ax = task_func(a, b)
    assert df.empty
    assert isinstance(ax, plt.Axes)
    assert ax.get_figure() is None

def test_task_func_non_empty_input():
    a = [1, 2, 3]
    b = [4, 5, 6]
    df, ax = task_func(a, b)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (3, 2)
    assert df.columns.tolist() == ['A', 'B']
    assert isinstance(ax, plt.Axes)
    plt.close(ax.get_figure())

def test_task_func_custom_columns():
    a = [1, 2, 3]
    b = [4, 5, 6]
    columns = ['X', 'Y']
    df, ax = task_func(a, b, columns=columns)
    assert df.columns.tolist() == columns
    plt.close(ax.get_figure())

def test_task_func_single_element():
    a = [1]
    b = [2]
    df, ax = task_func(a, b)
    assert df.shape == (1, 2)
    plt.close(ax.get_figure())

def test_task_func_negative_values():
    a = [-1, -2, -3]
    b = [-4, -5, -6]
    df, ax = task_func(a, b)
    assert df.shape == (3, 2)
    plt.close(ax.get_figure())