import pytest
from src_0950 import task_func
import numpy as np
import pandas as pd

def test_task_func_shape():
    rows, columns = 3, 4
    df = task_func(rows, columns)
    assert df.shape == (rows, columns)

def test_task_func_randomness():
    rows, columns = 3, 4
    seed = 42
    df1 = task_func(rows, columns, seed=seed)
    df2 = task_func(rows, columns, seed=seed)
    assert df1.equals(df2), "DataFrames should be equal with the same seed"

def test_task_func_default_seed():
    rows, columns = 3, 4
    df1 = task_func(rows, columns)
    df2 = task_func(rows, columns)
    assert not df1.equals(df2), "DataFrames should differ without a seed"

def test_task_func_with_zero_rows():
    rows, columns = 0, 4
    df = task_func(rows, columns)
    assert df.empty, "DataFrame should be empty with zero rows"

def test_task_func_with_zero_columns():
    rows, columns = 3, 0
    df = task_func(rows, columns)
    assert df.empty, "DataFrame should be empty with zero columns"

def test_task_func_with_negative_rows():
    rows, columns = -3, 4
    with pytest.raises(ValueError):
        task_func(rows, columns)

def test_task_func_with_negative_columns():
    rows, columns = 3, -4
    with pytest.raises(ValueError):
        task_func(rows, columns)