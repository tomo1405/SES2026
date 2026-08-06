import pytest
from src_0788 import task_func
import numpy as np

def test_task_func():
    # Test case 1: arrays with same length
    array1 = np.array([1, 2, 3])
    array2 = np.array([4, 5, 6])
    expected_result = 3
    assert task_func(array1, array2) == expected_result

    # Test case 2: arrays with different length
    array1 = np.array([1, 2, 3])
    array2 = np.array([4, 5])
    with pytest.raises(ValueError):
        task_func(array1, array2)

    # Test case 3: arrays with length 0
    array1 = np.array([])
    array2 = np.array([])
    expected_result = 0
    assert task_func(array1, array2) == expected_result

    # Test case 4: arrays with different shapes
    array1 = np.array([[1, 2], [3, 4]])
    array2 = np.array([[5, 6], [7, 8]])
    expected_result = 3
    assert task_func(array1, array2) == expected_result

    # Test case 5: arrays with different shapes and different length
    array1 = np.array([[1, 2], [3, 4]])
    array2 = np.array([[5, 6], [7, 8], [9, 10]])
    with pytest.raises(ValueError):
        task_func(array1, array2)