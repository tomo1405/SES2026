import pytest
from src_1081 import task_func

def test_task_func_with_valid_input():
    assert abs(task_func("2,500") - 250) < 1e-6

def test_task_func_with_zero_area():
    assert abs(task_func("0") - 0) < 1e-6

def test_task_func_with_large_area():
    assert abs(task_func("10,000") - 1000) < 1e-6

def test_task_func_with_non_numeric_area():
    with pytest.raises(ValueError):
        task_func("abc")

def test_task_func_with_empty_string():
    with pytest.raises(ValueError):
        task_func("")

def test_task_func_with_negative_area():
    with pytest.raises(ValueError):
        task_func("-1,000")