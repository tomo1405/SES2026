import pytest
from src_0002 import task_func

def test_task_func_default_length():
    result = task_func()
    assert len(result) <= 52, "The length of the result should be less than or equal to 52 (number of letters in the alphabet)."

def test_task_func_custom_length():
    length = 50
    result = task_func(length)
    assert len(result) <= 52, "The length of the result should be less than or equal to 52 (number of letters in the alphabet)."
    assert sum(result.values()) == length, f"The total count of all characters should be equal to the specified length {length}."

def test_task_func_zero_length():
    result = task_func(0)
    assert result == {}, "The result should be an empty dictionary for zero length."

def test_task_func_negative_length():
    with pytest.raises(ValueError):
        task_func(-1)

def test_task_func_all_uppercase():
    result = task_func(26)
    assert all(isinstance(value, int) and value >= 0 for value in result.values()), "All values in the result should be non-negative integers."
    assert len(result) <= 26, "The number of unique uppercase letters should not exceed 26."

def test_task_func_all_lowercase():
    result = task_func(26)
    assert all(isinstance(value, int) and value >= 0 for value in result.values()), "All values in the result should be non-negative integers."
    assert len(result) <= 26, "The number of unique lowercase letters should not exceed 26."

def test_task_func_mixed_case():
    result = task_func(50)
    assert all(isinstance(value, int) and value >= 0 for value in result.values()), "All values in the result should be non-negative integers."
    assert len(result) <= 52, "The number of unique letters (uppercase and lowercase) should not exceed 52."