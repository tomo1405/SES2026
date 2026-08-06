import pytest
from src_0312 import task_func

def test_task_func():
    # Test with empty list
    assert task_func([]) == {'mean': 0, 'median': 0, 'mode': 0}

    # Test with list of lists
    assert task_func([[1, 2, 3], [4, 5, 6]]) == {'mean': 3, 'median': 3, 'mode': 3}

    # Test with list of lists and size
    assert task_func([[1, 2, 3], [4, 5, 6]], size=10) == {'mean': 3, 'median': 3, 'mode': 3}

    # Test with list of lists and seed
    assert task_func([[1, 2, 3], [4, 5, 6]], seed=123) == {'mean': 3, 'median': 3, 'mode': 3}

    # Test with list of lists and size and seed
    assert task_func([[1, 2, 3], [4, 5, 6]], size=10, seed=123) == {'mean': 3, 'median': 3, 'mode': 3}