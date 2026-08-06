import pytest
from src_0125 import task_func

def test_task_func_type_error():
    with pytest.raises(TypeError):
        task_func(123)

def test_task_func_value_error():
    with pytest.raises(ValueError):
        task_func([1, 2, 3, 'a'])

def test_task_func_return_type():
    assert isinstance(task_func([1, 2, 3]), tuple)

def test_task_func_return_value():
    assert task_func([1, 2, 3]) == (12, 12)