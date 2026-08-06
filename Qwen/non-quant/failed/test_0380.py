import pytest
from src_0380 import task_func
import pandas as pd
import numpy as np

def test_task_func_length():
    length = 5
    df = task_func(length)
    assert len(df) == length, "The DataFrame length does not match the input length."

def test_task_func_columns():
    df = task_func(5)
    assert list(df.columns) == COLUMNS, "The DataFrame columns do not match the expected columns."

def test_task_func_data_type():
    df = task_func(5)
    assert isinstance(df, pd.DataFrame), "The returned object is not a DataFrame."

def test_task_func_random_values():
    df = task_func(5)
    assert df.values.dtype == np.int64, "The DataFrame values are not of integer type."
    assert df.values.min() >= 0 and df.values.max() <= 99, "The DataFrame values are not within the expected range (0-99)."

def test_task_func_empty_input():
    df = task_func(0)
    assert df.empty, "The DataFrame is not empty when the input length is 0."

def test_task_func_negative_length():
    with pytest.raises(ValueError):
        task_func(-1)