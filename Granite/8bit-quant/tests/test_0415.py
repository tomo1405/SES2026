import pandas as pd
import numpy as np
from src_0415 import task_func
import pytest

@pytest.fixture
def input_data():
    return [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def test_task_func(input_data):
    df, ax = task_func(input_data)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, np.ndarray) or ax is None

def test_task_func_with_invalid_column(input_data):
    df, ax = task_func(input_data, column="invalid_column")
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, np.ndarray) or ax is None

def test_task_func_with_no_numeric_data(input_data):
    df, ax = task_func(input_data, column="a")
    assert df.empty
    assert ax is None