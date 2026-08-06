import pandas as pd
import random
from src_0317 import task_func
import pytest

CATEGORIES = ['A', 'B', 'C', 'D', 'E']

def test_task_func():
    # Test with default value_range
    df = task_func()
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (5, 2)
    assert df.columns.tolist() == ['Category', 'Count']
    assert df['Category'].tolist() == CATEGORIES
    assert all(df['Count'] >= 0) and all(df['Count'] <= 100)

    # Test with custom value_range
    value_range = (10, 20)
    df = task_func(value_range=value_range)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (5, 2)
    assert df.columns.tolist() == ['Category', 'Count']
    assert df['Category'].tolist() == CATEGORIES
    assert all(df['Count'] >= 10) and all(df['Count'] <= 20)