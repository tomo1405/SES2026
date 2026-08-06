import pytest
from src_0498 import task_func

def test_task_func_positive():
    # Test with a positive days_in_past value
    result = task_func(days_in_past=7)
    assert result is not None

def test_task_func_negative():
    # Test with a negative days_in_past value
    with pytest.raises(ValueError):
        task_func(days_in_past=-1)

def test_task_func_zero():
    # Test with days_in_past set to zero
    result = task_func(days_in_past=0)
    assert result is not None

def test_task_func_weekday():
    # Test to check the weekday calculation
    result = task_func(days_in_past=7)
    assert result in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']