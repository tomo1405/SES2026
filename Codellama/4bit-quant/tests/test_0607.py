import pytest
from src_0607 import task_func
import pandas as pd
from scipy import stats

def test_task_func():
    # Test case 1: Test with a valid matrix
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected_output = pd.DataFrame([[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]])
    assert task_func(matrix).equals(expected_output)

    # Test case 2: Test with a matrix with NaN values
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, np.nan]]
    expected_output = pd.DataFrame([[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]])
    assert task_func(matrix).equals(expected_output)

    # Test case 3: Test with a matrix with a different shape
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
    expected_output = pd.DataFrame([[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]])
    assert task_func(matrix).equals(expected_output)

    # Test case 4: Test with a matrix with a different dtype
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected_output = pd.DataFrame([[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]])
    assert task_func(matrix).equals(expected_output)