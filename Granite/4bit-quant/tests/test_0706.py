import numpy as np
import pandas as pd
import pytest
from src_0706 import task_func


def test_task_func():
    df = pd.DataFrame({'A': np.random.rand(100)})
    column = 'A'
    alpha = 0.05
    assert task_func(df, column, alpha)

def test_task_func_column_not_in_df():
    df = pd.DataFrame({'A': np.random.rand(100)})
    column = 'B'
    alpha = 0.05
    with pytest.raises(ValueError):
        task_func(df, column, alpha)

def test_task_func_alpha_lt_0():
    df = pd.DataFrame({'A': np.random.rand(100)})
    column = 'A'
    alpha = -0.05
    with pytest.raises(ValueError):
        task_func(df, column, alpha)