import pytest
from src_0947 import task_func
import numpy as np
import pandas as pd

def test_task_func_default_values():
    df = task_func()
    assert df.shape == (3, 2)
    assert df.min().min() >= 0
    assert df.max().max() <= 100

def test_task_func_custom_dimensions():
    df = task_func(rows=5, cols=3)
    assert df.shape == (5, 3)

def test_task_func_min_max_equal():
    df = task_func(min_val=42, max_val=42)
    assert df.shape == (3, 2)
    assert df.values.flatten()[0] == 42

def test_task_func_custom_range():
    df = task_func(min_val=10, max_val=20)
    assert df.min().min() >= 10
    assert df.max().max() <= 20

def test_task_func_seed_consistency():
    df1 = task_func(seed=42)
    df2 = task_func(seed=42)
    assert df1.equals(df2)

def test_task_func_negative_values():
    df = task_func(min_val=-50, max_val=50)
    assert df.min().min() >= -50
    assert df.max().max() <= 50