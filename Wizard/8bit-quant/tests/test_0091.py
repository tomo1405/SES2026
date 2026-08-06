python
import numpy as np
import math
import pytest

from src_0091 import task_func

def test_task_func():
    # Test case 1
    data = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])
    target = [5, 6]
    k = 2
    expected_result = [[3, 4], [5, 6]]
    result = task_func(data, target, k)
    assert result == expected_result

    # Test case 2
    data = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])
    target = [5, 6]
    k = 3
    expected_result = [[3, 4], [5, 6], [7, 8]]
    result = task_func(data, target, k)
    assert result == expected_result

    # Test case 3
    data = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])
    target = [5, 6]
    k = 4
    expected_result = [[3, 4], [5, 6], [7, 8], [9, 10]]
    result = task_func(data, target, k)
    assert result == expected_result

    # Test case 4
    data = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])
    target = [5, 6]
    k = 5
    expected_result = [[3, 4], [5, 6], [7, 8], [9, 10]]
    result = task_func(data, target, k)
    assert result == expected_result

    # Test case 5
    data = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])
    target = [5, 6]
    k = 0
    expected_result = []
    result = task_func(data, target, k)
    assert result == expected_result

    # Test case 6
    data = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])
    target = [5, 6]
    k = -1
    with pytest.raises(ValueError):
        task_func(data, target, k)

    # Test case 7
    data = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])
    target = [5, 6]
    k = 1.5
    with pytest.raises(ValueError):
        task_func(data, target, k)

    # Test case 8
    data = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])
    target = [5, 6]
    k = "2"
    with pytest.raises(ValueError):
        task_func(data, target, k)

    # Test case 9
    data = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])
    target = [5, 6]
    k = None
    with pytest.raises(ValueError):
        task_func(data, target, k)