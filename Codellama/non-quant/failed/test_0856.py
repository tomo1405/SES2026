import pytest
from src_0856 import task_func

def test_task_func():
    n_strings = 10
    string_length = 10
    strings = task_func(n_strings, string_length)
    assert len(strings) == n_strings
    for string in strings:
        assert len(string) == string_length
        for char in string:
            assert char in VALID_CHARACTERS

def test_task_func_with_invalid_input():
    n_strings = -1
    string_length = 10
    with pytest.raises(ValueError):
        task_func(n_strings, string_length)

    n_strings = 10
    string_length = -1
    with pytest.raises(ValueError):
        task_func(n_strings, string_length)

    n_strings = 10
    string_length = 0
    with pytest.raises(ValueError):
        task_func(n_strings, string_length)