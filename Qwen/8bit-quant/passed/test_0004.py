import pytest
from src_0004 import task_func

def test_task_func():
    # Test with a simple list of letters
    letters = ['A', 'B', 'C']
    result = task_func(letters)
    
    # Check that the result is a dictionary
    assert isinstance(result, dict)
    
    # Check that each key in the result corresponds to a key in the input
    assert set(result.keys()) == set(letters)
    
    # Check that each value in the result is a float (mean of a list of integers)
    for value in result.values():
        assert isinstance(value, float)

    # Test with an empty list of letters
    letters = []
    result = task_func(letters)
    assert result == {}

    # Test with a single letter
    letters = ['X']
    result = task_func(letters)
    assert set(result.keys()) == {'X'}
    assert isinstance(result['X'], float)

    # Test with a larger list of letters
    letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    result = task_func(letters)
    assert set(result.keys()) == set(letters)
    for value in result.values():
        assert isinstance(value, float)