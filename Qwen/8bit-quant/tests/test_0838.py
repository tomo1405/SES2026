import pytest
from src_0838 import task_func
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

def test_task_func_default_columns():
    n_rows = 5
    scale_cols = [0, 2]
    df = task_func(n_rows, scale_cols)
    assert df.shape == (n_rows, 5)
    assert list(df.columns) == ['A', 'B', 'C', 'D', 'E']

def test_task_func_custom_columns():
    n_rows = 5
    scale_cols = [1, 3]
    columns = ['X', 'Y', 'Z', 'W']
    df = task_func(n_rows, scale_cols, columns=columns)
    assert df.shape == (n_rows, 4)
    assert list(df.columns) == columns

def test_task_func_random_seed():
    n_rows = 5
    scale_cols = [0]
    random_seed = 42
    df1 = task_func(n_rows, scale_cols, random_seed=random_seed)
    df2 = task_func(n_rows, scale_cols, random_seed=random_seed)
    assert df1.equals(df2)

def test_task_func_scaling():
    n_rows = 5
    scale_cols = [0]
    df = task_func(n_rows, scale_cols)
    original_data = df.iloc[:, 0].values
    scaled_data = StandardScaler().fit_transform(original_data.reshape(-1, 1)).flatten()
    assert np.allclose(df.iloc[:, 0].values, scaled_data)

def test_task_func_no_scaling():
    n_rows = 5
    scale_cols = []
    df = task_func(n_rows, scale_cols)
    assert np.allclose(df.values, np.random.randint(0, 100, size=(n_rows, 5)))

def test_task_func_empty_scale_cols():
    n_rows = 5
    scale_cols = []
    df = task_func(n_rows, scale_cols)
    assert df.shape == (n_rows, 5)
    assert list(df.columns) == ['A', 'B', 'C', 'D', 'E']