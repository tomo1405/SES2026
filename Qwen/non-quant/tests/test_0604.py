import pytest
from src_0604 import task_func
import numpy as np

def test_task_func():
    # Test with two 2x2 matrices
    matrix1 = np.array([[1, 2], [3, 4]])
    matrix2 = np.array([[5, 6], [7, 8]])
    expected_output = "1 2 5 6\n3 4 7 8"
    assert task_func(matrix1, matrix2) == expected_output

    # Test with matrices of different shapes
    matrix1 = np.array([[1, 2], [3, 4]])
    matrix2 = np.array([[5, 6, 7], [8, 9, 10]])
    expected_output = "1 2 5 6 7\n3 4 8 9 10"
    assert task_func(matrix1, matrix2) == expected_output

    # Test with one-dimensional arrays
    matrix1 = np.array([1, 2])
    matrix2 = np.array([3, 4, 5])
    expected_output = "1 2 3 4 5"
    assert task_func(matrix1, matrix2) == expected_output

    # Test with empty matrices
    matrix1 = np.array([])
    matrix2 = np.array([])
    expected_output = ""
    assert task_func(matrix1, matrix2) == expected_output

    # Test with one empty and one non-empty matrix
    matrix1 = np.array([])
    matrix2 = np.array([[1, 2], [3, 4]])
    expected_output = "1 2\n3 4"
    assert task_func(matrix1, matrix2) == expected_output

    matrix1 = np.array([[1, 2], [3, 4]])
    matrix2 = np.array([])
    expected_output = "1 2\n3 4"
    assert task_func(matrix1, matrix2) == expected_output