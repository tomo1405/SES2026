import pytest
from src_0440 import task_func
import numpy as np
import seaborn as sns

def test_task_func():
    # Test case 1: Basic input
    P = np.array([[1, 2], [3, 4]])
    T = np.array([[5, 6], [7, 8]])
    expected_result = np.array([[58, 64], [139, 154]])
    result, heatmap = task_func(P, T)
    assert np.array_equal(result, expected_result)
    assert isinstance(heatmap, sns.axisgrid.HeatMap)

    # Add more test cases as needed