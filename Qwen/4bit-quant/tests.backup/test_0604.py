import pytest
from src_0604 import task_func
import numpy as np
import pandas as pd

def test_task_func_with_valid_matrices():
    matrix1 = np.array([[1, 2], [3, 4]])
    matrix2 = np.array([[5, 6], [7, 8]])
    expected_output = "1 2 5 6\n3 4 7 8"
    assert task_func(matrix1, matrix2) == expected_output

def test_task_func_with_empty_matrices():
    matrix1 = np.array([])
    matrix2 = np.array([])
    expected_output = ""
    assert task_func(matrix1, matrix2) == expected_output

def test_task_func_with_one_empty_matrix():
    matrix1 = np.array([[1, 2], [3, 4]])
    matrix2 = np.array([])
    expected_output = "1 2\n3 4"
    assert task_func(matrix1, matrix2) == expected_output

def test_task_func_with_different_number_of_rows():
    with pytest.raises(ValueError):
        matrix1 = np.array([[1, 2]])
        matrix2 = np.array([[3, 4], [5, 6]])
        task_func(matrix1, matrix2)

def test_task_func_with_non_numeric_data():
    with pytest.raises(TypeError):
        matrix1 = np.array([["a", "b"], ["c", "d"]])
        matrix2 = np.array([[1, 2], [3, 4]])
        task_func(matrix1, matrix2)