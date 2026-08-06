import pytest
from src_0947 import task_func
import numpy as np
import pandas as pd

def test_task_func_default():
    df = task_func()
    assert df.shape == (3, 2)
    assert df.values.min() >= 0
    assert df.values.max() <= 100

def test_task_func_custom_shape():
    df = task_func(rows=5, cols=4)
    assert df.shape == (5, 4)

def test_task_func_min_max_equal():
    df = task_func(min_val=50, max_val=50)
    assert df.shape == (3, 2)
    assert (df.values == 50).all()

def test_task_func_min_max_values():
    df = task_func(min_val=10, max_val=20)
    assert df.values.min() >= 10
    assert df.values.max() <= 20

def test_task_func_seed():
    df1 = task_func(seed=1)
    df2 = task_func(seed=1)
    assert df1.equals(df2)

def test_task_func_no_randomness():
    df1 = task_func(seed=2)
    df2 = task_func(seed=2)
    assert df1.equals(df2)