import pytest
from src_0897 import task_func

def test_task_func():
    # Test case 1: Basic functionality test
    result = task_func(length=3, count=2, seed=123)
    expected = Counter({'a': 3, 'b': 3})
    assert result == expected

    # Add more test cases as needed