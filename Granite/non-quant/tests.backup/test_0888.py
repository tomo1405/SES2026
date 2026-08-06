import pandas as pd
import numpy as np
import itertools
from src_0888 import task_func

def test_task_func():
    T1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    df = task_func(T1)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (50, 9)
    assert all(df.columns == [f'Col_{i+1}' for i in range(9)])

def test_task_func_with_seed():
    T1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    seed = 42
    df1 = task_func(T1, seed=seed)
    df2 = task_func(T1, seed=seed)
    assert df1.equals(df2)

def test_task_func_with_row_num():
    T1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    row_num = 100
    df = task_func(T1, row_num=row_num)
    assert df.shape == (100, 9)