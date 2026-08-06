import pytest
from src_0834 import task_func
from statistics import mode
from collections import Counter

def test_task_func_default_values():
    result_mode, result_numbers = task_func()
    assert isinstance(result_mode, int)
    assert isinstance(result_numbers, Counter.items)

def test_task_func_custom_values():
    list_length = 50
    range_start = 10
    range_end = 20
    random_seed = 42
    expected_mode, expected_numbers = task_func(list_length, range_start, range_end, random_seed)
    
    # Verify mode
    assert isinstance(expected_mode, int)
    assert expected_mode in range(range_start, range_end + 1)
    
    # Verify numbers
    assert isinstance(expected_numbers, Counter.items)
    for number, count in expected_numbers:
        assert isinstance(number, int)
        assert isinstance(count, int)
        assert count > 0
        assert number in range(range_start, range_end + 1)

def test_task_func_with_seed():
    random_seed = 0
    _, numbers = task_func(random_seed=random_seed)
    assert isinstance(numbers, Counter.items)

def test_task_func_with_no_seed():
    _, numbers = task_func()
    assert isinstance(numbers, Counter.items)

def test_task_func_with_small_range():
    list_length = 10
    range_start = 1
    range_end = 1
    random_seed = 42
    expected_mode, expected_numbers = task_func(list_length, range_start, range_end, random_seed)
    
    # Verify mode
    assert expected_mode == 1
    
    # Verify numbers
    assert len(list(expected_numbers)) == 1
    for number, count in expected_numbers:
        assert number == 1
        assert count == 10

def test_task_func_with_large_range():
    list_length = 100
    range_start = 1
    range_end = 100
    random_seed = 42
    expected_mode, expected_numbers = task_func(list_length, range_start, range_end, random_seed)
    
    # Verify mode
    assert isinstance(expected_mode, int)
    assert expected_mode in range(range_start, range_end + 1)
    
    # Verify numbers
    assert isinstance(expected_numbers, Counter.items)
    for number, count in expected_numbers:
        assert isinstance(number, int)
        assert isinstance(count, int)
        assert count > 0
        assert number in range(range_start, range_end + 1)