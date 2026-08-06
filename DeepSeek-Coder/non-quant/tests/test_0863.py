import pytest
from src_0863 import task_func

def test_task_func():
    # Test with seed to ensure reproducibility
    result = task_func(5, seed=42)
    expected = {'a': ['a'], 'b': ['b'], 'c': ['c'], 'd': ['d'], 'e': ['e']}
    assert result == expected

    # Additional tests can be added to cover different scenarios