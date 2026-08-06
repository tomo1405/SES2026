import pytest
from src_0012 import task_func

def test_task_func():
    T1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    max_value = 100
    expected_p25 = 25
    expected_p50 = 50
    expected_p75 = 75

    p25, p50, p75 = task_func(T1, max_value)

    assert p25 == expected_p25
    assert p50 == expected_p50
    assert p75 == expected_p75

def test_task_func_with_different_max_value():
    T1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    max_value = 200
    expected_p25 = 25
    expected_p50 = 50
    expected_p75 = 75

    p25, p50, p75 = task_func(T1, max_value)

    assert p25 == expected_p25
    assert p50 == expected_p50
    assert p75 == expected_p75

def test_task_func_with_empty_list():
    T1 = []
    max_value = 100
    expected_p25 = 0
    expected_p50 = 0
    expected_p75 = 0

    p25, p50, p75 = task_func(T1, max_value)

    assert p25 == expected_p25
    assert p50 == expected_p50
    assert p75 == expected_p75

def test_task_func_with_invalid_input():
    T1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    max_value = -1
    expected_p25 = 0
    expected_p50 = 0
    expected_p75 = 0

    p25, p50, p75 = task_func(T1, max_value)

    assert p25 == expected_p25
    assert p50 == expected_p50
    assert p75 == expected_p75