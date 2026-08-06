import string

from src_0395 import task_func


def test_task_func_length():
    length = 10
    result = task_func(length)
    assert len(result) <= length, "The number of unique characters should not exceed the length of the string"

def test_task_func_seed():
    length = 10
    seed = 42
    result1 = task_func(length, seed)
    result2 = task_func(length, seed)
    assert result1 == result2, "The function should produce the same output for the same seed"

def test_task_func_character_set():
    length = 10
    result = task_func(length)
    for char in result:
        assert char in string.ascii_letters, "All characters should be ASCII letters"

def test_task_func_empty_string():
    length = 0
    result = task_func(length)
    assert result == {}, "An empty string should return an empty dictionary"

def test_task_func_single_character():
    length = 1
    result = task_func(length)
    assert len(result) == 1, "A single character string should return a dictionary with one entry"