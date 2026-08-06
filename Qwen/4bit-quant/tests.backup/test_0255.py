import pytest
from src_0255 import task_func

def test_task_func_with_default_precision():
    assert task_func(16) == '"4.0"'

def test_task_func_with_custom_precision():
    assert task_func(8, precision=3) == '"2.829"'

def test_task_func_with_decimal_value():
    assert task_func(2) == '"1.41"'

def test_task_func_with_zero():
    assert task_func(0) == '"0.0"'

def test_task_func_with_negative_value():
    with pytest.raises(ValueError):
        task_func(-4)

def test_task_func_with_large_number():
    assert task_func(1000000) == '"1000.0"'