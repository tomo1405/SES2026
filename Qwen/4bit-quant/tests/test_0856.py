import string

from src_0856 import task_func


def test_task_func_output_type():
    result = task_func(1, 10)
    assert isinstance(result, dict)

def test_task_func_character_count():
    result = task_func(1, 10)
    assert all(isinstance(k, str) and len(k) == 1 for k in result.keys())

def test_task_func_correct_number_of_strings():
    n_strings = 5
    result = task_func(n_strings, 10)
    concatenated_string = ''.join(result.keys())
    assert len(concatenated_string) == n_strings * 10

def test_task_func_valid_characters():
    result = task_func(1, 10)
    valid_characters = set(string.ascii_letters + string.digits)
    assert all(char in valid_characters for char in ''.join(result.keys()))

def test_task_func_with_zero_strings():
    result = task_func(0, 10)
    assert result == {}

def test_task_func_with_zero_length():
    result = task_func(5, 0)
    assert result == {}

def test_task_func_with_large_input():
    result = task_func(100, 100)
    assert len(result) <= len(string.ascii_letters + string.digits)