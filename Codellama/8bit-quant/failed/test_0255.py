import pytest
from src_0255 import task_func

def test_task_func():
    # Test case 1: square root of 16
    decimal_value = 16
    precision = 2
    expected_result = '4.00'
    actual_result = task_func(decimal_value, precision)
    assert actual_result == expected_result

    # Test case 2: square root of 25
    decimal_value = 25
    precision = 2
    expected_result = '5.00'
    actual_result = task_func(decimal_value, precision)
    assert actual_result == expected_result

    # Test case 3: square root of 100
    decimal_value = 100
    precision = 2
    expected_result = '10.00'
    actual_result = task_func(decimal_value, precision)
    assert actual_result == expected_result

    # Test case 4: square root of 1000
    decimal_value = 1000
    precision = 2
    expected_result = '31.62'
    actual_result = task_func(decimal_value, precision)
    assert actual_result == expected_result

    # Test case 5: square root of 10000
    decimal_value = 10000
    precision = 2
    expected_result = '100.00'
    actual_result = task_func(decimal_value, precision)
    assert actual_result == expected_result