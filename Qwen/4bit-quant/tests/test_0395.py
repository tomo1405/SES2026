import string

from src_0395 import task_func


def test_task_func_length():
    length = 10
    result = task_func(length)
    assert len(result) <= length, "The number of unique characters should not exceed the length"

def test_task_func_with_seed():
    length = 5
    seed = 42
    result1 = task_func(length, seed)
    result2 = task_func(length, seed)
    assert result1 == result2, "The results should be the same for the same seed"

def test_task_func_alphabetical_characters():
    length = 10
    result = task_func(length)
    for char in result:
        assert char in string.ascii_letters, "All characters should be alphabetical"

def test_task_func_zero_length():
    length = 0
    result = task_func(length)
    assert result == {}, "Result should be an empty dictionary for zero length"

def test_task_func_large_length():
    length = 1000
    result = task_func(length)
    assert len(result) <= length, "The number of unique characters should not exceed the length"