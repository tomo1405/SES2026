import pytest
from src_0336 import task_func

def test_task_func_default_length():
    result = task_func()
    assert len(result) <= 5  # Only letters from LETTERS can be present
    for letter, count in result.items():
        assert letter in ['a', 'b', 'c', 'd', 'e']
        assert isinstance(count, int)
        assert count > 0

def test_task_func_custom_length():
    length = 200
    result = task_func(length)
    assert len(result) <= 5  # Only letters from LETTERS can be present
    for letter, count in result.items():
        assert letter in ['a', 'b', 'c', 'd', 'e']
        assert isinstance(count, int)
        assert count > 0

def test_task_func_empty_string():
    length = 0
    result = task_func(length)
    assert len(result) == 0

def test_task_func_single_letter():
    length = 1
    result = task_func(length)
    assert len(result) == 1
    for letter, count in result.items():
        assert letter in ['a', 'b', 'c', 'd', 'e']
        assert isinstance(count, int)
        assert count == 1

def test_task_func_all_same_letters():
    length = 100
    result = task_func(length)
    assert len(result) == 1  # All letters are the same, so only one unique letter
    for letter, count in result.items():
        assert letter in ['a', 'b', 'c', 'd', 'e']
        assert isinstance(count, int)
        assert count == length

def test_task_func_sorted_by_frequency():
    result = task_func()
    counts = list(result.values())
    assert counts == sorted(counts, reverse=True)