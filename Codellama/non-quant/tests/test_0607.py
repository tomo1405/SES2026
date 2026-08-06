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

    # Test case 3: Test with a matrix with negative values
    matrix = [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]
    expected_output = pd.DataFrame([[-1.0, -2.0, -3.0], [-4.0, -5.0, -6.0], [-7.0, -8.0, -9.0]])
    assert task_func(matrix).equals(expected_output)

    # Test case 4: Test with a matrix with positive values
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected_output = pd.DataFrame([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]])
    assert task_func(matrix).equals(expected_output)

    # Test case 5: Test with a matrix with a mix of positive and negative values
    matrix = [[-1, 2, 3], [4, -5, 6], [7, 8, -9]]
    expected_output = pd.DataFrame([[-1.0, 2.0, 3.0], [4.0, -5.0, 6.0], [7.0, 8.0, -9.0]])
    assert task_func(matrix).equals(expected_output)