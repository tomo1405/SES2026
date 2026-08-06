import pytest
from src_1026 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def test_task_func_empty_input():
    data_dict = {}
    df, ax = task_func(data_dict)
    assert df.empty
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == "Scaled Values"

def test_task_func_single_row():
    data_dict = {'A': [1], 'B': [2]}
    df, ax = task_func(data_dict)
    assert df.equals(pd.DataFrame({'A': [1], 'B': [2]}))
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == "Scaled Values"

def test_task_func_multiple_rows():
    data_dict = {'A': [1, 2, 3], 'B': [4, 5, 6]}
    df, ax = task_func(data_dict)
    expected_df = pd.DataFrame({'A': [0, 0.5, 1], 'B': [0, 0.5, 1]})
    assert df.equals(expected_df)
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == "Scaled Values"

def test_task_func_with_nan():
    data_dict = {'A': [1, np.nan, 3], 'B': [4, 5, np.nan]}
    df, ax = task_func(data_dict)
    expected_df = pd.DataFrame({'A': [0, 1], 'B': [0, 1]})
    assert df.equals(expected_df)
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == "Scaled Values"