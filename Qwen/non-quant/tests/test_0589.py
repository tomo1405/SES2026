import numpy as np
import pandas as pd
from src_0589 import task_func


def test_task_func_returns_dataframe():
    df = task_func()
    assert isinstance(df, pd.DataFrame), "The function should return a pandas DataFrame."

def test_dataframe_columns():
    df = task_func()
    expected_columns = ['X', 'Y']
    assert list(df.columns) == expected_columns, f"The DataFrame columns should be {expected_columns}."

def test_dataframe_size():
    df = task_func()
    expected_size = (SIZE, 2)
    assert df.shape == expected_size, f"The DataFrame shape should be {expected_size}."

def test_dataframe_values_range():
    df = task_func()
    assert df['X'].between(0, RANGE-1).all(), "All values in column 'X' should be within the range [0, RANGE)."
    assert df['Y'].between(0, RANGE-1).all(), "All values in column 'Y' should be within the range [0, RANGE)."

def test_dataframe_values_types():
    df = task_func()
    assert df['X'].dtype == np.int64, "Column 'X' should contain integer values."
    assert df['Y'].dtype == np.int64, "Column 'Y' should contain integer values."