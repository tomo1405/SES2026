import pytest
from src_0091 import task_func

def test_task_func():
    data = np.array([[1, 2], [3, 4], [5, 6]])
    target = [1, 2]
    k = 2
    expected_result = [[1, 2], [3, 4]]
    assert task_func(data, target, k) == expected_result

def test_task_func_invalid_k():
    data = np.array([[1, 2], [3, 4], [5, 6]])
    target = [1, 2]
    k = -1
    with pytest.raises(ValueError):
        task_func(data, target, k)

def test_task_func_invalid_data():
    data = np.array([[1, 2], [3, 4], [5, 6]])
    target = [1, 2]
    k = 2
    data = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
    with pytest.raises(ValueError):
        task_func(data, target, k)

def test_task_func_invalid_target():
    data = np.array([[1, 2], [3, 4], [5, 6]])
    target = [1, 2, 3]
    k = 2
    with pytest.raises(ValueError):
        task_func(data, target, k)