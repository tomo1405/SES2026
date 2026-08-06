import pytest
from src_0701 import task_func
import pandas as pd
import numpy as np

def test_task_func():
    data = [[1, 2], [3, 4]]
    cols = ['a', 'b']
    expected_result = pd.DataFrame([[1, 2], [3, 4]], columns=cols)
    result = task_func(data, cols)
    assert result.equals(expected_result)

def test_task_func_with_different_data():
    data = [[1, 2], [3, 4]]
    cols = ['a', 'b']
    expected_result = pd.DataFrame([[1, 2], [3, 4]], columns=cols)
    result = task_func(data, cols)
    assert result.equals(expected_result)

def test_task_func_with_different_cols():
    data = [[1, 2], [3, 4]]
    cols = ['a', 'b']
    expected_result = pd.DataFrame([[1, 2], [3, 4]], columns=cols)
    result = task_func(data, cols)
    assert result.equals(expected_result)

def test_task_func_with_different_data_and_cols():
    data = [[1, 2], [3, 4]]
    cols = ['a', 'b']
    expected_result = pd.DataFrame([[1, 2], [3, 4]], columns=cols)
    result = task_func(data, cols)
    assert result.equals(expected_result)