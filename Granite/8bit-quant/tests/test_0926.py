import pandas as pd
import numpy as np
import pytest
from src_0926 import task_func

def test_task_func():
    df = task_func()
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (1000, 5)
    assert df.columns.tolist() == ['A', 'B', 'C', 'D', 'E']
    assert df.isnull().sum().sum() == 0
    assert (df < -1).sum().sum() == 400

def test_task_func_with_custom_args():
    df = task_func(data_size=500, column_names=['X', 'Y', 'Z'], seed=42)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (500, 3)
    assert df.columns.tolist() == ['X', 'Y', 'Z']
    assert df.isnull().sum().sum() == 0
    assert (df < -1).sum().sum() == 150

def test_task_func_with_invalid_args():
    with pytest.raises(ValueError):
        df = task_func(data_size=-100)
    with pytest.raises(ValueError):
        df = task_func(column_names=['A', 'B', 123])
    with pytest.raises(ValueError):
        df = task_func(seed='abc')