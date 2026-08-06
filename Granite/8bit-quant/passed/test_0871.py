import pandas as pd
import numpy as np
import itertools
from src_0871 import task_func

def test_task_func():
    data_list = [('a', 1, 2.1), ('b', 2, 3.2), ('c', 3, 4.3), ('d', 4, 5.4), ('e', 5, 6.5)]
    df = task_func(data_list)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (5, 1)
    assert df.columns.tolist() == ['Mean Value']
    assert df.index.tolist() == ['Position 0', 'Position 1', 'Position 2', 'Position 3', 'Position 4']
    assert df['Mean Value'].tolist() == [3.0, 3.0, 3.0, 3.0, 3.0]

def test_task_func_with_missing_values():
    data_list = [('a', 1, 2.1), ('b', 2, np.nan), ('c', 3, 4.3), ('d', 4, 5.4), ('e', np.nan, 6.5)]
    df = task_func(data_list)
    assert df['Mean Value'].tolist() == [2.1, 3.2, 4.3, 5.4, 6.5]

def test_task_func_with_non_numeric_values():
    data_list = [('a', 1, 2.1), ('b', 2, 'abc'), ('c', 3, 4.3), ('d', 4, 5.4), ('e', 5, 6.5)]
    df = task_func(data_list)
    assert df['Mean Value'].tolist() == [3.0, np.nan, 3.0, 3.0, 3.0]