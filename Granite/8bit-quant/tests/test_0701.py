import pandas as pd
import numpy as np
import pytest
from src_0701 import task_func

def test_task_func():
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    cols = ['A', 'B', 'C']
    expected_correlation_matrix = np.array([[1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [1.0, 1.0, 1.0]])
    
    correlation_matrix = task_func(data, cols)
    
    assert np.array_equal(correlation_matrix, expected_correlation_matrix)