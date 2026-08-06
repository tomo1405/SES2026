import pytest
from src_0834 import task_func

def test_task_func():
    # Test case 1: list_length = 1000, range_start = 1, range_end = 10, random_seed = None
    expected_mode = 5
    expected_numbers = [(1, 100), (2, 100), (3, 100), (4, 100), (5, 100), (6, 100), (7, 100), (8, 100), (9, 100), (10, 100)]
    actual_mode, actual_numbers = task_func(list_length=1000, range_start=1, range_end=10, random_seed=None)
    assert actual_mode == expected_mode
    assert actual_numbers == expected_numbers

    # Test case 2: list_length = 1000, range_start = 1, range_end = 10, random_seed = 1234
    expected_mode = 5
    expected_numbers = [(1, 100), (2, 100), (3, 100), (4, 100), (5, 100), (6, 100), (7, 100), (8, 100), (9, 100), (10, 100)]
    actual_mode, actual_numbers = task_func(list_length=1000, range_start=1, range_end=10, random_seed=1234)
    assert actual_mode == expected_mode
    assert actual_numbers == expected_numbers

    # Test case 3: list_length = 1000, range_start = 1, range_end = 10, random_seed = 4321
    expected_mode = 5
    expected_numbers = [(1, 100), (2, 100), (3, 100), (4, 100), (5, 100), (6, 100), (7, 100), (8, 100), (9, 100), (10, 100)]
    actual_mode, actual_numbers = task_func(list_length=1000, range_start=1, range_end=10, random_seed=4321)
    assert actual_mode == expected_mode
    assert actual_numbers == expected_numbers

    # Test case 4: list_length = 1000, range_start = 1, range_end = 10, random_seed = 123456789
    expected_mode = 5
    expected_numbers = [(1, 100), (2, 100), (3, 100), (4, 100), (5, 100), (6, 100), (7, 100), (8, 100), (9, 100), (10, 100)]
    actual_mode, actual_numbers = task_func(list_length=1000, range_start=1, range_end=10, random_seed=123456789)
    assert actual_mode == expected_mode
    assert actual_numbers == expected_numbers