import pytest
from src_0767 import task_func

def test_task_func_type_error():
    with pytest.raises(TypeError):
        task_func(123)

def test_task_func_patterns_type_error():
    with pytest.raises(TypeError):
        task_func("abc", patterns=123)

def test_task_func_patterns_value_error():
    with pytest.raises(ValueError):
        task_func("abc", patterns=["abc", 123])

def test_task_func_return_type():
    assert isinstance(task_func("abc", patterns=["abc"]), dict)

def test_task_func_return_value():
    assert task_func("abc", patterns=["abc"]) == {"abc": 1}