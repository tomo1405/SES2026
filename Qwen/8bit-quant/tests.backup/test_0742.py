import pytest
from src_0742 import task_func

def test_task_func():
    # Test with empty dictionary
    assert task_func({}) == {}

    # Test with single item
    assert task_func({'a1': 10}) == {'a': 10}

    # Test with multiple items with the same starting key
    assert task_func({'a1': 10, 'a2': 20, 'a3': 30}) == {'a': 60}

    # Test with multiple items with different starting keys
    assert task_func({'a1': 10, 'b2': 20, 'c3': 30}) == {'a': 10, 'b': 20, 'c': 30}

    # Test with mixed case keys
    assert task_func({'A1': 10, 'a2': 20, 'B3': 30}) == {'A': 10, 'a': 20, 'B': 30}

    # Test with numeric keys
    assert task_func({'1a': 10, '1b': 20, '2c': 30}) == {'1': 30, '2': 30}

    # Test with special characters
    assert task_func({'@1': 10, '#2': 20, '$3': 30}) == {'@': 10, '#': 20, '$': 30}