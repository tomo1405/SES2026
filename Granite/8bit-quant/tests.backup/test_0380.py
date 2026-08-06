import pandas as pd
import numpy as np
from src_0380 import task_func
import pytest

def test_task_func_with_valid_input():
    length = 10
    df = task_func(length)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (length, len(COLUMNS))

def test_task_func_with_invalid_input():
    with pytest.raises(TypeError):
        task_func("invalid input")

def test_task_func_with_zero_length():
    df = task_func(0)
    assert df.shape == (0, len(COLUMNS))

def test_task_func_with_negative_length():
    with pytest.raises(ValueError):
        task_func(-1)