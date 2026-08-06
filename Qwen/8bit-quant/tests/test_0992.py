import string

from src_0992 import task_func


def test_task_func_length():
    length = 10
    result = task_func(length)
    assert len(result) == length // 2

def test_task_func_content():
    length = 20
    result = task_func(length)
    assert all(c in string.printable for c in result)

def test_task_func_empty_input():
    length = 0
    result = task_func(length)
    assert result == ""

def test_task_func_odd_length():
    length = 15
    result = task_func(length)
    assert len(result) == length // 2

def test_task_func_repeated_calls():
    length = 5
    results = [task_func(length) for _ in range(5)]
    assert len(set(results)) > 1  # Check that results are not identical

def test_task_func_non_ascii_characters():
    length = 20
    result = task_func(length)
    assert all(ord(c) < 128 for c in result)  # Ensure only ASCII characters