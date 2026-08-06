import pytest
from src_0549 import task_func

def test_task_func():
    result = task_func()
    assert isinstance(result, str), "The result should be a string"
    assert len(result) > 0, "The result should not be an empty string"

def test_task_func_with_custom_length():
    custom_length = 50
    result = task_func(custom_length)
    assert isinstance(result, str), "The result should be a string"
    assert len(result) > 0, "The result should not be an empty string"

def test_task_func_reproducibility():
    # Since the function uses random, we can't predict the exact output,
    # but we can check if it returns the same type and non-empty string.
    result1 = task_func()
    result2 = task_func()
    assert isinstance(result1, str), "The first result should be a string"
    assert isinstance(result2, str), "The second result should be a string"
    assert len(result1) > 0, "The first result should not be an empty string"
    assert len(result2) > 0, "The second result should not be an empty string"
    assert result1 != result2, "The results should be different due to randomness"

def test_task_func_with_zero_length():
    with pytest.raises(ValueError):
        task_func(0)

def test_task_func_with_negative_length():
    with pytest.raises(ValueError):
        task_func(-10)