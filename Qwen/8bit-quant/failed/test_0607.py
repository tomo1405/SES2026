import pytest
from src_0607 import task_func
import pandas as pd
import numpy as np

def test_task_func_with_valid_data():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    expected_output = pd.DataFrame({
        0: [0.0, 0.0, 0.0],
        1: [0.0, 0.0, 0.0],
        2: [0.0, 0.0, 0.0]
    })
    result = task_func(matrix)
    pd.testing.assert_frame_equal(result, expected_output)

def test_task_func_with_nan_values():
    matrix = [
        [1, 2, np.nan],
        [4, 5, 6],
        [7, 8, 9]
    ]
    expected_output = pd.DataFrame({
        0: [0.0, 0.0, 0.0],
        1: [0.0, 0.0, 0.0],
        2: [0.0, 0.0, 0.0]
    })
    result = task_func(matrix)
    pd.testing.assert_frame_equal(result, expected_output)

def test_task_func_with_empty_matrix():
    matrix = []
    expected_output = pd.DataFrame()
    result = task_func(matrix)
    pd.testing.assert_frame_equal(result, expected_output)

def test_task_func_with_single_row():
    matrix = [[1, 2, 3]]
    expected_output = pd.DataFrame({
        0: [0.0],
        1: [0.0],
        2: [0.0]
    })
    result = task_func(matrix)
    pd.testing.assert_frame_equal(result, expected_output)

def test_task_func_with_single_column():
    matrix = [
        [1],
        [2],
        [3]
    ]
    expected_output = pd.DataFrame({
        0: [0.0, 0.0, 0.0]
    })
    result = task_func(matrix)
    pd.testing.assert_frame_equal(result, expected_output)