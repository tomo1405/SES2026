import pytest
from src_0002 import task_func

def test_task_func_default_length():
    result = task_func()
    assert len(result) <= 52  # Maximum possible unique characters in the default length of 100

def test_task_func_custom_length():
    length = 50
    result = task_func(length)
    assert len(result) <= 52  # Maximum possible unique characters in the custom length of 50

def test_task_func_zero_length():
    result = task_func(0)
    assert result == {}

def test_task_func_negative_length():
    with pytest.raises(ValueError):
        task_func(-1)

def test_task_func_all_uppercase():
    random.seed(0)  # For reproducibility
    result = task_func(10)
    assert all(key.isupper() for key in result.keys())

def test_task_func_all_lowercase():
    random.seed(1)  # For reproducibility
    result = task_func(10)
    assert all(key.islower() for key in result.keys())

def test_task_func_mixed_case():
    random.seed(2)  # For reproducibility
    result = task_func(10)
    assert any(key.isupper() for key in result.keys())
    assert any(key.islower() for key in result.keys())

def test_task_func_sum_of_counts_equals_length():
    length = 100
    result = task_func(length)
    assert sum(result.values()) == length

def test_task_func_unique_characters():
    length = 52
    result = task_func(length)
    assert len(result) == 52  # All characters are unique