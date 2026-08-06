python
import numpy as np
import pandas as pd
import pytest

def task_func(matrix1, matrix2):
    combined_matrix = np.concatenate((matrix1, matrix2), axis=1)
    df = pd.DataFrame(combined_matrix)
    return df.to_string(index=False, header=False)

def test_task_func():
    matrix1 = np.array([[1, 2], [3, 4]])
    matrix2 = np.array([[5, 6], [7, 8]])
    expected_result = "1 2 5 6\n3 4 7 8"
    assert task_func(matrix1, matrix2) == expected_result