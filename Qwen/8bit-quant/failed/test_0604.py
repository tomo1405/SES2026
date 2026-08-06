import pytest
from src_0604 import task_func
import numpy as np

def test_task_func():
    # Test with 2x2 matrices
    matrix1 = np.array([[1, 2], [3, 4]])
    matrix2 = np.array([[5, 6], [7, 8]])
    expected_output = "1 2 5 6\n3 4 7 8"
    assert task_func(matrix1, matrix2) == expected_output

    # Test with different shapes
    matrix1 = np.array([[1, 2], [3, 4], [5, 6]])
    matrix2 = np.array([[7, 8]])
    expected_output = "1 2 7 8\n3 4 7 8\n5 6 7 8"
    assert task_func(matrix1, matrix2) == expected_output

    # Test with empty matrices
    matrix1 = np.array([])
    matrix2 = np.array([])
    expected_output = ""
    assert task_func(matrix1, matrix2) == expected_output

    # Test with one empty matrix
    matrix1 = np.array([[1, 2], [3, 4]])
    matrix2 = np.array([])
    expected_output = "1 2\n3 4"
    assert task_func(matrix1, matrix2) == expected_output

    # Test with non-integer values
    matrix1 = np.array([[1.1, 2.2], [3.3, 4.4]])
    matrix2 = np.array([[5.5, 6.6], [7.7, 8.8]])
    expected_output = "1.1 2.2 5.5 6.6\n3.3 4.4 7.7 8.8"
    assert task_func(matrix1, matrix2) == expected_output