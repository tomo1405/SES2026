import math

from src_0748 import task_func


def test_task_func_no_numbers():
    result = task_func("No numbers here")
    assert result == (0, 0.0)

def test_task_func_single_integer():
    result = task_func("The number is 42")
    assert result == (1, math.sqrt(42))

def test_task_func_single_float():
    result = task_func("The number is 3.14")
    assert math.isclose(result[1], math.sqrt(3.14), rel_tol=1e-9)

def test_task_func_multiple_numbers():
    result = task_func("Numbers are 16 and 9.0 and 4")
    assert result == (3, math.sqrt(16) + math.sqrt(9.0) + math.sqrt(4))

def test_task_func_mixed_numbers():
    result = task_func("Mix of 1, 2.25, and 3.0")
    assert math.isclose(result[1], math.sqrt(1) + math.sqrt(2.25) + math.sqrt(3.0), rel_tol=1e-9)

def test_task_func_negative_numbers():
    result = task_func("Negative numbers -1 and -4.0 are not included")
    assert result == (0, 0.0)

def test_task_func_zero():
    result = task_func("Zero is 0")
    assert result == (1, math.sqrt(0))

def test_task_func_large_numbers():
    result = task_func("Large numbers 1000000 and 1000000.0")
    assert result == (2, math.sqrt(1000000) + math.sqrt(1000000.0))