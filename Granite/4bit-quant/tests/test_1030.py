import pandas as pd
import numpy as np
import pytest

from src_1030 import task_func

def test_task_func():
    df = task_func()
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (100, 3)
    assert all(df.columns == ['a', 'b', 'c'])

def test_task_func_with_custom_args():
    df = task_func(rows=50, columns=5)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (50, 5)
    assert all(df.columns == ['a', 'b', 'c', 'd', 'e'])