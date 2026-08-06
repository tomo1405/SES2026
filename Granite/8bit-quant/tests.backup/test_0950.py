import numpy as np
import pandas as pd
from src_0950 import task_func
import pytest

def test_task_func_default_args():
    """
    Test the task_func function with default arguments.
    """
    rows = 10
    columns = 5
    df = task_func(rows, columns)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (rows, columns)

def test_task_func_seed():
    """
    Test the task_func function with a specified seed.
    """
    rows = 10
    columns = 5
    seed = 42
    df1 = task_func(rows, columns, seed)
    df2 = task_func(rows, columns, seed)
    assert isinstance(df1, pd.DataFrame)
    assert isinstance(df2, pd.DataFrame)
    assert df1.shape == (rows, columns)
    assert df2.shape == (rows, columns)
    assert df1.equals(df2)

def test_task_func_invalid_args():
    """
    Test the task_func function with invalid arguments.
    """
    with pytest.raises(ValueError):
        task_func(-1, 5)
    with pytest.raises(ValueError):
        task_func(10, -5)
    with pytest.raises(TypeError):
        task_func('a', 5)
    with pytest.raises(TypeError):
        task_func(10, 'b')