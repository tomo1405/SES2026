import numpy as np
import seaborn as sns
from src_0440 import task_func
import pytest

def test_task_func():
    P = np.array([[1, 2], [3, 4]])
    T = np.array([[5, 6], [7, 8]])
    expected_result = np.array([[19, 22], [43, 50]])
    expected_heatmap = sns.heatmap(expected_result)

    result, heatmap = task_func(P, T)

    assert np.array_equal(result, expected_result)
    assert heatmap == expected_heatmap