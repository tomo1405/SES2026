import numpy as np
import pandas as pd
from src_0607 import task_func


def test_task_func():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected_output = pd.DataFrame([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]])
    actual_output = task_func(matrix)
    assert actual_output.equals(expected_output)

def test_task_func_with_nan_values():
    matrix = [[1, 2, 3], [4, np.nan, 6], [7, 8, 9]]
    expected_output = pd.DataFrame([[1.0, 2.0, 3.0], [4.0, 0.0, 6.0], [7.0, 8.0, 9.0]])
    actual_output = task_func(matrix)
    assert actual_output.equals(expected_output)