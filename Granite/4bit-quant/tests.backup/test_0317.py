import pandas as pd
import random
from src_0317 import task_func

# Constants
CATEGORIES = ['A', 'B', 'C', 'D', 'E']

def test_task_func():
    # Test case 1: Default value range
    df = task_func()
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (5, 2)
    assert df.columns.tolist() == ['Category', 'Count']
    assert df['Category'].tolist() == CATEGORIES
    assert all(df['Count'] >= 0) and all(df['Count'] <= 100)

    # Test case 2: Custom value range
    value_range = (1, 10)
    df = task_func(value_range=value_range)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (5, 2)
    assert df.columns.tolist() == ['Category', 'Count']
    assert df['Category'].tolist() == CATEGORIES
    assert all(df['Count'] >= 1) and all(df['Count'] <= 10)