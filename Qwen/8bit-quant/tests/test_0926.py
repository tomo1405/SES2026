import pytest
from src_0926 import task_func
import pandas as pd
import numpy as np

def test_task_func_default_values():
    df = task_func()
    assert df.shape == (1000, 5)
    assert list(df.columns) == ['A', 'B', 'C', 'D', 'E']

def test_task_func_custom_data_size():
    df = task_func(data_size=500)
    assert df.shape == (500, 5)

def test_task_func_custom_column_names():
    df = task_func(column_names=['X', 'Y', 'Z'])
    assert df.shape == (1000, 3)
    assert list(df.columns) == ['X', 'Y', 'Z']

def test_task_func_custom_seed():
    df1 = task_func(seed=42)
    df2 = task_func(seed=42)
    assert df1.equals(df2)

def test_task_func_value_replacement():
    df = task_func()
    assert (df[df < 10] == -1).all().all()

def test_task_func_value_range():
    df = task_func()
    assert (df >= -1).all().all()
    assert (df <= 100).all().all()