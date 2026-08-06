import pytest
from src_0498 import task_func

def test_task_func_with_positive_days_in_past():
    days_in_past = 7
    expected_weekday = "Sunday"
    assert task_func(days_in_past) == expected_weekday

def test_task_func_with_negative_days_in_past():
    days_in_past = -1
    with pytest.raises(ValueError):
        task_func(days_in_past)