import random
import statistics
from src_0003 import task_func
import pytest

def test_task_func():
    # Test case 1: Test with an empty input
    result = task_func([])
    assert result == {}

    # Test case 2: Test with a single letter
    result = task_func(['A'])
    assert result == {'A': [random.randint(0, 100) for _ in range(random.randint(1, 10))]}

    # Test case 3: Test with multiple letters
    result = task_func(['A', 'B', 'C'])
    assert isinstance(result, dict)
    assert all(letter in result for letter in ['A', 'B', 'C'])
    assert all(isinstance(value, list) for value in result.values())
    assert all(isinstance(item, int) for value in result.values() for item in value)

    # Test case 4: Test with a large number of letters
    result = task_func([chr(i) for i in range(65, 65 + 26)])
    assert isinstance(result, dict)
    assert all(letter in result for letter in [chr(i) for i in range(65, 65 + 26)])
    assert all(isinstance(value, list) for value in result.values())
    assert all(isinstance(item, int) for value in result.values() for item in value)
    assert all(0 <= item <= 100 for value in result.values() for item in value)