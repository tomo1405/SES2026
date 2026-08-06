import math

from src_0748 import task_func


def test_task_func_no_numbers():
    result = task_func("No numbers here!")
    assert result == (0, 0.0)

def test_task_func_single_integer():
    result = task_func("The number is 42.")
    assert result == (1, math.sqrt(42))

def test_task_func_single_float():
    result = task_func("The number is 3.14.")
    assert math.isclose(result[1], math.sqrt(3.14), rel_tol=1e-9)

def test_task_func_multiple_numbers():
    result = task_func("Numbers 16, 9 and 4.")
    assert result == (3, math.sqrt(16) + math.sqrt(9) + math.sqrt(4))

def test_task_func_mixed_integers_and_floats():
    result = task_func("Mix of 25, 3.6 and 1.")
    assert math.isclose(result[1], math.sqrt(25) + math.sqrt(3.6) + math.sqrt(1), rel_tol=1e-9)

def test_task_func_with_negative_numbers():
    result = task_func("Negative numbers -4 and -9.")
    assert result == (0, 0.0)  # No valid square roots for negative numbers

def test_task_func_with_zero():
    result = task_func("Zero is 0.")
    assert math.isclose(result[1], math.sqrt(0), rel_tol=1e-9)

def test_task_func_empty_string():
    result = task_func("")
    assert result == (0, 0.0)