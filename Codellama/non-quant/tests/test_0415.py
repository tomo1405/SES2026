import pytest
from src_0415 import task_func
import pandas as pd
import numpy as np

def test_task_func_with_valid_data():
    data = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    df, ax = task_func(data)
    assert df.equals(data)
    assert ax is not None

def test_task_func_with_invalid_data():
    data = pd.DataFrame({"a": ["a", "b", "c"], "b": ["d", "e", "f"]})
    df, ax = task_func(data)
    assert df.equals(data)
    assert ax is None

def test_task_func_with_empty_data():
    data = pd.DataFrame()
    df, ax = task_func(data)
    assert df.equals(data)
    assert ax is None

def test_task_func_with_non_numeric_data():
    data = pd.DataFrame({"a": ["a", "b", "c"], "b": ["d", "e", "f"]})
    df, ax = task_func(data)
    assert df.equals(data)
    assert ax is None