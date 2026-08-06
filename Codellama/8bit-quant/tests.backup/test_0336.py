import pytest
from src_0336 import task_func

def test_task_func():
    # Test with default string length
    result = task_func()
    assert isinstance(result, collections.OrderedDict)
    assert all(isinstance(key, str) and isinstance(value, int) for key, value in result.items())
    assert all(key in LETTERS for key in result.keys())
    assert all(value >= 0 for value in result.values())

    # Test with custom string length
    result = task_func(string_length=50)
    assert isinstance(result, collections.OrderedDict)
    assert all(isinstance(key, str) and isinstance(value, int) for key, value in result.items())
    assert all(key in LETTERS for key in result.keys())
    assert all(value >= 0 for value in result.values())

    # Test with empty string
    result = task_func(string_length=0)
    assert isinstance(result, collections.OrderedDict)
    assert len(result) == 0