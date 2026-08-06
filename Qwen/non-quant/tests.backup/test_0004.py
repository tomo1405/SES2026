import pytest
from src_0004 import task_func

def test_task_func():
    # Test with a small set of letters
    letters = ['A', 'B', 'C']
    result = task_func(letters)
    
    # Check that the result is a dictionary
    assert isinstance(result, dict)
    
    # Check that each key in the result corresponds to a key in the input
    assert set(result.keys()) == set(letters)
    
    # Check that each value is a float (mean of integers)
    for value in result.values():
        assert isinstance(value, float)

def test_task_func_empty_input():
    # Test with an empty list of letters
    letters = []
    result = task_func(letters)
    
    # Check that the result is an empty dictionary
    assert result == {}

def test_task_func_single_letter():
    # Test with a single letter
    letters = ['X']
    result = task_func(letters)
    
    # Check that the result is a dictionary with one key
    assert len(result) == 1
    assert 'X' in result
    
    # Check that the value is a float
    assert isinstance(result['X'], float)

def test_task_func_randomness():
    # Test the randomness by running the function multiple times
    letters = ['A', 'B']
    results = [task_func(letters) for _ in range(5)]
    
    # Check that each run produces different results
    assert len(set(map(str, results))) > 1