import pytest
from src_0604 import task_func
import numpy as np
import pandas as pd

def test_task_func():
    matrix1 = np.array([[1, 2], [3, 4]])
    matrix2 = np.array([[5, 6], [7, 8]])
    result = task_func(matrix1, matrix2)
    expected_result = "1 2 5 6\n3 4 7 8"
    assert result == expected_result