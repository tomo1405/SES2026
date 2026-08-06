import pytest
from src_0498 import task_func

def test_task_func_default_days():
    # Test with default value of days_in_past (7)
    expected_weekday = (datetime.now(pytz.UTC) - timedelta(days=7)).strftime('%A')
    assert task_func() == expected_weekday

def test_task_func_custom_days():
    # Test with a custom number of days in the past
    days_in_past = 10
    expected_weekday = (datetime.now(pytz.UTC) - timedelta(days=days_in_past)).strftime('%A')
    assert task_func(days_in_past) == expected_weekday

def test_task_func_zero_days():
    # Test with zero days in the past
    expected_weekday = datetime.now(pytz.UTC).strftime('%A')
    assert task_func(0) == expected_weekday

def test_task_func_negative_days():
    # Test with negative days in the past, should raise ValueError
    with pytest.raises(ValueError, match="Days in the past cannot be negative"):
        task_func(-5)

def test_task_func_edge_case_max_int():
    # Test with maximum possible integer value for days_in_past
    # This is more of a theoretical test since it's unlikely to be practical
    with pytest.raises(OverflowError):
        task_func(2**31 - 1)

def test_task_func_edge_case_min_int():
    # Test with minimum possible integer value for days_in_past
    # This is more of a theoretical test since it's unlikely to be practical
    with pytest.raises(OverflowError):
        task_func(-(2**31 - 1))