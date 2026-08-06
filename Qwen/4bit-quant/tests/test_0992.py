import string

from src_0992 import task_func


def test_task_func_length():
    length = 10
    result = task_func(length)
    assert len(result) == length // 2, f"Expected length of {length // 2}, got {len(result)}"

def test_task_func_characters():
    length = 10
    result = task_func(length)
    assert all(c in string.printable for c in result), "Result contains non-printable characters"

def test_task_func_randomness():
    length = 10
    results = [task_func(length) for _ in range(5)]
    assert len(set(results)) > 1, "Function does not seem to produce random results"

def test_task_func_empty_input():
    length = 0
    result = task_func(length)
    assert result == "", "Expected empty string for length 0"

def test_task_func_odd_length():
    length = 9
    result = task_func(length)
    assert len(result) == length // 2, f"Expected length of {length // 2}, got {len(result)}"