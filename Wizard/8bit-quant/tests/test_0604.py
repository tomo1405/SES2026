python
import numpy as np
import pandas as pd
import pytest

def task_func(matrix1, matrix2):
    combined_matrix = np.concatenate((matrix1, matrix2), axis=1)
    df = pd.DataFrame(combined_matrix)
    return df.to_string(index=False, header=False)

def test_task_func():
    matrix1 = np.array([[1, 2, 3], [4, 5, 6]])
    matrix2 = np.array([[7, 8, 9], [10, 11, 12]])
    expected_result = "1 2 3 7 8 9\n4 5 6 10 11 12"
    assert task_func(matrix1, matrix2) == expected_result