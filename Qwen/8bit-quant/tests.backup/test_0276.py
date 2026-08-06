import pytest
from src_0276 import task_func

def test_task_func_positive_integer():
    assert task_func(1) == [(1, 2)]
    assert task_func(2) == [(1, 2), (1, 3), (2, 3)]
    assert task_func(3) == [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]

def test_task_func_value_error():
    with pytest.raises(ValueError):
        task_func(0)
    with pytest.raises(ValueError):
        task_func(-1)
    with pytest.raises(ValueError):
        task_func(-10)

def test_task_func_large_number():
    result = task_func(5)
    expected = [(1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 4), (3, 5), (4, 5)]
    assert result == expected

def test_task_func_type_error():
    with pytest.raises(TypeError):
        task_func(1.5)
    with pytest.raises(TypeError):
        task_func("string")
    with pytest.raises(TypeError):
        task_func(None)