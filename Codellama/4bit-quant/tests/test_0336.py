import collections

import pytest
from src_0336 import task_func


def test_task_func():
    # Test with default string length
    sorted_freq = task_func()
    assert isinstance(sorted_freq, collections.OrderedDict)
    assert all(isinstance(key, str) and isinstance(value, int) for key, value in sorted_freq.items())
    assert all(key in LETTERS for key in sorted_freq.keys())
    assert all(value >= 0 for value in sorted_freq.values())

    # Test with custom string length
    sorted_freq = task_func(string_length=50)
    assert isinstance(sorted_freq, collections.OrderedDict)
    assert all(isinstance(key, str) and isinstance(value, int) for key, value in sorted_freq.items())
    assert all(key in LETTERS for key in sorted_freq.keys())
    assert all(value >= 0 for value in sorted_freq.values())

    # Test with invalid string length
    with pytest.raises(ValueError):
        sorted_freq = task_func(string_length=-1)