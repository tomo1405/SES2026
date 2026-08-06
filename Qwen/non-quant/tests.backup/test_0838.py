import pytest
from src_0838 import task_func
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

def test_task_func_output_shape():
    n_rows = 10
    scale_cols = [0, 2]
    df = task_func(n_rows, scale_cols)
    assert df.shape == (n_rows, 5)

def test_task_func_column_names():
    n_rows = 10
    scale_cols = [0, 2]
    df = task_func(n_rows, scale_cols)
    assert list(df.columns) == ['A', 'B', 'C', 'D', 'E']

def test_task_func_scaled_columns():
    n_rows = 10
    scale_cols = [0, 2]
    df = task_func(n_rows, scale_cols)
    
    for col_index in scale_cols:
        original_data = np.random.randint(0, 100, size=n_rows)
        scaler = StandardScaler()
        scaled_data = scaler.fit_transform(original_data.reshape(-1, 1)).flatten()
        
        assert np.allclose(df.iloc[:, col_index].values, scaled_data, atol=1e-7)

def test_task_func_random_seed():
    n_rows = 10
    scale_cols = [0, 2]
    random_seed = 42
    df1 = task_func(n_rows, scale_cols, random_seed=random_seed)
    df2 = task_func(n_rows, scale_cols, random_seed=random_seed)
    assert df1.equals(df2)

def test_task_func_no_scaling():
    n_rows = 10
    scale_cols = []
    df = task_func(n_rows, scale_cols)
    assert df.equals(pd.DataFrame(np.random.randint(0, 100, size=(n_rows, 5)), columns=['A', 'B', 'C', 'D', 'E']))

def test_task_func_single_scale_column():
    n_rows = 10
    scale_cols = [1]
    df = task_func(n_rows, scale_cols)
    scaler = StandardScaler()
    original_data = np.random.randint(0, 100, size=n_rows)
    scaled_data = scaler.fit_transform(original_data.reshape(-1, 1)).flatten()
    assert np.allclose(df.iloc[:, 1].values, scaled_data, atol=1e-7)