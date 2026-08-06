import pytest
from src_0701 import task_func
import pandas as pd
import numpy as np

def test_task_func():
    data = [[1, 2], [3, 4]]
    cols = ['A', 'B']
    expected_correlation_matrix = pd.DataFrame([[1, 0], [0, 1]], index=cols, columns=cols)
    correlation_matrix = task_func(data, cols)
    assert np.array_equal(correlation_matrix, expected_correlation_matrix)