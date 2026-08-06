import numpy as np
import pytest
from src_0810 import task_func


def test_task_func():
    data = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
    n_clusters = 2
    expected_output = {0: np.array([0, 2]), 1: np.array([1, 3])}
    actual_output = task_func(data, n_clusters)
    assert actual_output == expected_output

def test_task_func_with_invalid_input():
    data = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
    n_clusters = 5
    with pytest.raises(ValueError):
        task_func(data, n_clusters)