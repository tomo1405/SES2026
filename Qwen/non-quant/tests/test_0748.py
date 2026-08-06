import math

from src_0748 import task_func


def test_task_func_no_numbers():
    result = task_func("No numbers here!")
    assert result == (0, 0.0)

def test_task_func_single_integer():
    result = task_func("The number is 42")
    assert result == (1, math.sqrt(42))

def test_task_func_single_float():
    result = task_func("The number is 3.14")
    assert math.isclose(result[1], math.sqrt(3.14))

def test_task_func_multiple_numbers():
    result = task_func("Numbers 16 and 9 are here")
    assert result == (2, math.sqrt(16) + math.sqrt(9))

def test_task_func_mixed_numbers():
    result = task_func("Mix of 4, 2.5, and 9")
    assert math.isclose(result[1], math.sqrt(4) + math.sqrt(2.5) + math.sqrt(9))

def test_task_func_negative_numbers():
    result = task_func("Negative numbers -4 and -9 are not valid")
    assert result == (0, 0.0)

def test_task_func_zero():
    result = task_func("Zero is 0")
    assert result == (1, 0.0)