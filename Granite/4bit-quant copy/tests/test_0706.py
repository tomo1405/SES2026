import numpy as np
from scipy import stats
from src_0706 import task_func
import pandas as pd

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