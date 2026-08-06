import pytest
from src_0810 import task_func
import numpy as np

def test_task_func_with_two_clusters():
    data = np.array([[1, 2], [1, 4], [1, 0],
                     [4, 2], [4, 4], [4, 0]])
    n_clusters = 2
    expected_output = {0: np.array([0, 1, 2]), 1: np.array([3, 4, 5])}
    assert task_func(data, n_clusters) == expected_output

def test_task_func_with_one_cluster():
    data = np.array([[1, 2], [1, 4], [1, 0],
                     [4, 2], [4, 4], [4, 0]])
    n_clusters = 1
    expected_output = {0: np.array([0, 1, 2, 3, 4, 5])}
    assert task_func(data, n_clusters) == expected_output

def test_task_func_with_three_clusters():
    data = np.array([[1, 2], [1, 4], [1, 0],
                     [4, 2], [4, 4], [4, 0],
                     [7, 2], [7, 4], [7, 0]])
    n_clusters = 3
    output = task_func(data, n_clusters)
    assert len(output) == 3
    for i in range(3):
        assert i in output

def test_task_func_empty_data():
    data = np.array([])
    n_clusters = 1
    expected_output = {0: np.array([])}
    assert task_func(data, n_clusters) == expected_output

def test_task_func_single_point():
    data = np.array([[1, 2]])
    n_clusters = 1
    expected_output = {0: np.array([0])}
    assert task_func(data, n_clusters) == expected_output

def test_task_func_invalid_n_clusters():
    data = np.array([[1, 2], [1, 4], [1, 0]])
    n_clusters = 0
    with pytest.raises(ValueError):
        task_func(data, n_clusters)

    n_clusters = -1
    with pytest.raises(ValueError):
        task_func(data, n_clusters)