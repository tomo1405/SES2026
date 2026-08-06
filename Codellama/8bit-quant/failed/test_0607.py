import pytest
from src_0607 import task_func
import pandas as pd
from scipy import stats

def test_task_func():
    # Test case 1: Normal input
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected_output = pd.DataFrame([[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]])
    assert task_func(matrix).equals(expected_output)

    # Test case 2: Input with NaN values
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, np.nan]]
    expected_output = pd.DataFrame([[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]])
    assert task_func(matrix).equals(expected_output)

    # Test case 3: Input with non-numeric values
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, "a"]]
    expected_output = pd.DataFrame([[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]])
    assert task_func(matrix).equals(expected_output)

    # Test case 4: Input with different data types
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9.0]]
    expected_output = pd.DataFrame([[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]])
    assert task_func(matrix).equals(expected_output)

    # Test case 5: Input with different shapes
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected_output = pd.DataFrame([[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]])
    assert task_func(matrix).equals(expected_output)