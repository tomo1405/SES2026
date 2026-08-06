import numpy as np
import pandas as pd
from src_0604 import task_func

def test_task_func():
    matrix1 = np.array([[1, 2, 3], [4, 5, 6]])
    matrix2 = np.array([[7, 8, 9], [10, 11, 12]])
    expected_output = "1 2 3 7 8 9n4 5 6 10 11 12n"
    actual_output = task_func(matrix1, matrix2)
    assert actual_output == expected_output

def test_task_func_with_empty_matrix():
    matrix1 = np.array([])
    matrix2 = np.array([[7, 8, 9], [10, 11, 12]])
    expected_output = "7 8 9n10 11 12n"
    actual_output = task_func(matrix1, matrix2)
    assert actual_output == expected_output

def test_task_func_with_one_matrix():
    matrix1 = np.array([[1, 2, 3], [4, 5, 6]])
    matrix2 = np.array([])
    expected_output = "1 2 3n4 5 6n"
    actual_output = task_func(matrix1, matrix2)
    assert actual_output == expected_output