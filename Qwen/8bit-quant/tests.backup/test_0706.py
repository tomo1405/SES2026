import pytest
from src_0706 import task_func
import pandas as pd
import numpy as np

def test_task_func_column_exists():
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    assert task_func(df, 'A', 0.05) == True

def test_task_func_column_does_not_exist():
    df = pd.DataFrame({'A': [1, 2, 3]})
    with pytest.raises(ValueError, match='Column does not exist in DataFrame'):
        task_func(df, 'B', 0.05)

def test_task_func_alpha_zero():
    df = pd.DataFrame({'A': [1, 2, 3]})
    assert task_func(df, 'A', 0) == False

def test_task_func_alpha_one():
    df = pd.DataFrame({'A': [1, 2, 3]})
    assert task_func(df, 'A', 1) == True

def test_task_func_all_zeros():
    df = pd.DataFrame({'A': [0, 0, 0]})
    assert task_func(df, 'A', 0.05) == True

def test_task_func_all_ones():
    df = pd.DataFrame({'A': [1, 1, 1]})
    assert task_func(df, 'A', 0.05) == True

def test_task_func_negative_values():
    df = pd.DataFrame({'A': [-1, -2, -3]})
    assert task_func(df, 'A', 0.05) == True

def test_task_func_mixed_values():
    df = pd.DataFrame({'A': [1, -2, 3]})
    assert task_func(df, 'A', 0.05) == True

def test_task_func_large_data():
    df = pd.DataFrame({'A': np.random.randn(1000)})
    assert isinstance(task_func(df, 'A', 0.05), bool)