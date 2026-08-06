import pytest
from src_0122 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def test_task_func_input_type():
    with pytest.raises(TypeError):
        task_func("not a list")

def test_task_func_output_type():
    df, ax = task_func([1, 2, 3])
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)

def test_task_func_output_columns():
    df, _ = task_func([1, 2, 3])
    assert list(df.columns) == ['Category', 'Sales']

def test_task_func_output_shape():
    df, _ = task_func([1, 2, 3])
    assert df.shape == (5, 2)

def test_task_func_output_values():
    df, _ = task_func([1, 2, 3])
    assert all(df['Category'].isin(['Electronics', 'Fashion', 'Home & Kitchen', 'Automotive', 'Sports']))
    assert all(df['Sales'] > 0)

def test_task_func_randomness():
    df1, _ = task_func([1, 2, 3], seed=42)
    df2, _ = task_func([1, 2, 3], seed=42)
    assert df1.equals(df2)

def test_task_func_append_value():
    df, _ = task_func([1, 2, 3])
    assert 12 in df.values