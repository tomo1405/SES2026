import pytest
from src_0604 import task_func
import numpy as np
import pandas as pd

def test_task_func():
    matrix1 = np.array([[1, 2], [3, 4]])
    matrix2 = np.array([[5, 6], [7, 8]])
    expected_output = "1 2 5 6\n3 4 7 8"
    assert task_func(matrix1, matrix2) == expected_output

def test_task_func_with_different_axis():
    matrix1 = np.array([[1, 2], [3, 4]])
    matrix2 = np.array([[5, 6], [7, 8]])
    expected_output = "1 2 3 4\n5 6 7 8"
    assert task_func(matrix1, matrix2, axis=0) == expected_output

def test_task_func_with_invalid_axis():
    matrix1 = np.array([[1, 2], [3, 4]])
    matrix2 = np.array([[5, 6], [7, 8]])
    with pytest.raises(ValueError):
        task_func(matrix1, matrix2, axis=2)