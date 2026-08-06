import pytest
from src_1078 import task_func

def test_task_func_with_empty_list():
    assert task_func([], "UTC") == 0.0

def test_task_func_with_single_element_list():
    assert task_func(["12/01/20 12:00:00.0"], "UTC") == 0.0

def test_task_func_with_two_elements_list():
    assert task_func(["12/01/20 12:00:00.0", "12/01/20 12:00:01.0"], "UTC") == 1.0

def test_task_func_with_three_elements_list():
    assert task_func(["12/01/20 12:00:00.0", "12/01/20 12:00:01.0", "12/01/20 12:00:02.0"], "UTC") == 1.0

def test_task_func_with_different_timezones():
    assert task_func(["12/01/20 12:00:00.0", "12/01/20 12:00:01.0"], "UTC") == 1.0
    assert task_func(["12/01/20 12:00:00.0", "12/01/20 12:00:01.0"], "America/New_York") == 1.0
    assert task_func(["12/01/20 12:00:00.0", "12/01/20 12:00:01.0"], "Asia/Tokyo") == 1.0

def test_task_func_with_invalid_time_strings():
    with pytest.raises(ValueError):
        task_func(["12/01/20 12:00:00.0", "12/01/20 12:00:01.0", "invalid_time_string"], "UTC")