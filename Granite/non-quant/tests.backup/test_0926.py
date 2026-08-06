import pandas as pd
import numpy as np
from src_0926 import task_func
import pytest

def test_task_func_default_args():
    df = task_func()
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (1000, 5)
    assert df.columns.tolist() == ['A', 'B', 'C', 'D', 'E']
    assert df.loc[0, 'A'] == -1

def test_task_func_custom_args():
    df = task_func(data_size=500, column_names=['X', 'Y', 'Z'], seed=42)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (500, 3)
    assert df.columns.tolist() == ['X', 'Y', 'Z']
    assert df.loc[0, 'X'] == -1

def test_task_func_invalid_args():
    with pytest.raises(ValueError):
        task_func(data_size=-100)
    with pytest.raises(ValueError):
        task_func(column_names=['A', 'B'])
    with pytest.raises(ValueError):
        task_func(seed='abc')