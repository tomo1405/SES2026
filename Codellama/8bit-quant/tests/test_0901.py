import pytest
from src_0901 import task_func

def test_task_func_input_type():
    with pytest.raises(ValueError):
        task_func(1)

def test_task_func_input_value():
    with pytest.raises(ValueError):
        task_func([1, 2, 3])

def test_task_func_output_type():
    assert isinstance(task_func([]), dict)

def test_task_func_output_value():
    assert task_func([]) == {'x': None, 'y': None, 'z': None}

def test_task_func_output_value_with_data():
    data = [{'x': 1, 'y': 2, 'z': 3}, {'x': 4, 'y': 5, 'z': 6}]
    expected_output = {'x': {'mean': 2.5, 'sum': 5, 'max': 4, 'min': 1, 'std': 1.5811388300841898},
                      'y': {'mean': 3.5, 'sum': 7, 'max': 5, 'min': 2, 'std': 1.5811388300841898},
                      'z': {'mean': 4.5, 'sum': 9, 'max': 6, 'min': 3, 'std': 1.5811388300841898}}
    assert task_func(data) == expected_output