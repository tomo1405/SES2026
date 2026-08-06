import pytest
from src_0026 import task_func

def test_task_func():
    data_dict = {"name": "John Doe", "age": 30}
    expected_result = "eJxLy8jNgjAUAOw=="
    assert task_func(data_dict) == expected_result

def test_task_func_invalid_input():
    data_dict = {"name": "John Doe", "age": "invalid"}
    with pytest.raises(TypeError):
        task_func(data_dict)

def test_task_func_empty_input():
    data_dict = {}
    with pytest.raises(ValueError):
        task_func(data_dict)