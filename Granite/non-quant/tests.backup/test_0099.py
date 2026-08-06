import pytest
from src_0099 import task_func

def test_task_func():
    num_strings = 10
    string_length = 5
    result = task_func(num_strings, string_length)
    assert isinstance(result, list)
    assert all(isinstance(item, tuple) and len(item) == 2 for item in result)
    assert all(isinstance(item[0], str) and isinstance(item[1], int) for item in result)