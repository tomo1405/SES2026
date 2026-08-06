import pytest
from src_0742 import task_func

def test_task_func():
    # Test with an empty dictionary
    assert task_func({}) == {}

    # Test with a single key-value pair
    assert task_func({'a1': 10}) == {'a': 10}

    # Test with multiple keys starting with the same character
    assert task_func({'a1': 10, 'a2': 20, 'a3': 30}) == {'a': 60}

    # Test with keys starting with different characters
    assert task_func({'a1': 10, 'b2': 20, 'c3': 30}) == {'a': 10, 'b': 20, 'c': 30}

    # Test with mixed case keys
    assert task_func({'A1': 10, 'a2': 20, 'B3': 30}) == {'A': 10, 'a': 20, 'B': 30}

    # Test with numeric keys
    assert task_func({1: 10, 2: 20, 3: 30}) == {'1': 10, '2': 20, '3': 30}

    # Test with complex keys
    assert task_func({('a', 1): 10, ('a', 2): 20, ('b', 3): 30}) == {'a': 30, 'b': 30}