import pandas as pd
import os
import numpy as np
import ast
from src_0073 import task_func
def test_task_func_with_csv_file():
    directory = 'path/to/directory'
    df, hist = task_func(directory)
    assert isinstance(df, pd.DataFrame)
    assert 'email' in df.columns
    assert 'list' in df.columns
    assert 'sum' in df.columns
    assert 'mean' in df.columns
    assert 'median' in df.columns
    assert isinstance(hist, matplotlib.axes.Axes)
def test_task_func_with_no_csv_file():
    directory = 'path/to/empty/directory'
    df, hist = task_func(directory)
    assert isinstance(df, pd.DataFrame)
    assert df.empty
    assert isinstance(hist, matplotlib.axes.Axes)
def test_task_func_with_multiple_csv_files():
    directory = 'path/to/directory'
    for i in range(2, 10):
        with open(os.path.join(directory, f'file_{i}.csv'), 'w') as f:
            pass
    df, hist = task_func(directory)
    assert isinstance(df, pd.DataFrame)
    assert 'email' in df.columns
    assert 'list' in df.columns
    assert 'sum' in df.columns
    assert 'mean' in df.columns
    assert 'median' in df.columns
    assert isinstance(hist, matplotlib.axes.Axes)