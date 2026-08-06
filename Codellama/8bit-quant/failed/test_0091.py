import pytest
from src_0091 import task_func

def test_task_func_valid_input():
    data = np.array([[1, 2], [3, 4], [5, 6]])
    target = [1, 2]
    k = 2
    expected_output = [[1, 2], [3, 4]]
    assert task_func(data, target, k) == expected_output

def test_task_func_invalid_input():
    data = np.array([[1, 2], [3, 4], [5, 6]])
    target = [1, 2]
    k = -1
    with pytest.raises(ValueError):
        task_func(data, target, k)

def test_task_func_invalid_input_type():
    data = np.array([[1, 2], [3, 4], [5, 6]])
    target = [1, 2]
    k = "2"
    with pytest.raises(TypeError):
        task_func(data, target, k)

def test_task_func_invalid_input_value():
    data = np.array([[1, 2], [3, 4], [5, 6]])
    target = [1, 2]
    k = 100
    with pytest.raises(ValueError):
        task_func(data, target, k)