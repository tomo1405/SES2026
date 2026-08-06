import pytest
from src_0255 import task_func

def test_task_func_positive_value():
    assert task_func(16) == '"4.0"'

def test_task_func_non_perfect_square():
    assert task_func(18) == '"4.24"'

def test_task_func_zero():
    assert task_func(0) == '"0.0"'

def test_task_func_with_precision():
    assert task_func(2, precision=3) == '"1.414"'

def test_task_func_negative_value():
    with pytest.raises(ValueError):
        task_func(-4)

def test_task_func_large_number():
    assert task_func(1000000) == '"1000.0"'