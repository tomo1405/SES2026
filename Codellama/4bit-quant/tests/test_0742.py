import pytest
from src_0742 import task_func

def test_task_func():
    # Test case 1: Empty dictionary
    assert task_func({}) == {}

    # Test case 2: Single key-value pair
    assert task_func({'a': 1}) == {'a': 1}

    # Test case 3: Multiple key-value pairs with the same first character
    assert task_func({'a': 1, 'b': 2, 'c': 3}) == {'a': 6, 'b': 2, 'c': 3}

    # Test case 4: Multiple key-value pairs with different first characters
    assert task_func({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}) == {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

    # Test case 5: Dictionary with non-string keys
    assert task_func({1: 1, 2: 2, 3: 3}) == {1: 1, 2: 2, 3: 3}

    # Test case 6: Dictionary with non-numeric values
    assert task_func({'a': 'a', 'b': 'b', 'c': 'c'}) == {'a': 'a', 'b': 'b', 'c': 'c'}

    # Test case 7: Dictionary with mixed keys and values
    assert task_func({'a': 1, 2: 'b', 'c': 'c'}) == {'a': 1, 2: 'b', 'c': 'c'}