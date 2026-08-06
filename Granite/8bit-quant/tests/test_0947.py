import pytest
from src_0947 import task_func
import numpy as np
import pandas as pd
import random

def test_task_func_default_args():
    df = task_func()
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (3, 2)
    assert (df.values >= 0).all() and (df.values <= 100).all()

def test_task_func_custom_args():
    rows = 5
    cols = 4
    min_val = -100
    max_val = 100
    seed = 123
    random.seed(seed)
    np.random.seed(seed)
    df = task_func(rows, cols, min_val, max_val, seed)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (rows, cols)
    assert (df.values >= min_val).all() and (df.values <= max_val).all()

def test_task_func_min_max_equal():
    rows = 10
    cols = 8
    min_val = 50
    max_val = 50
    seed = 456
    random.seed(seed)
    np.random.seed(seed)
    df = task_func(rows, cols, min_val, max_val, seed)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (rows, cols)
    assert (df.values == min_val).all()