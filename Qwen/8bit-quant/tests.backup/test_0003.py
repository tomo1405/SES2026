import pytest
from src_0003 import task_func

def test_task_func():
    # Test with a simple input
    letters = ['A', 'B', 'C']
    result = task_func(letters)
    
    # Check if the result is a dictionary
    assert isinstance(result, dict)
    
    # Check if all keys from the input are in the result
    assert set(result.keys()) == set(letters)
    
    # Check if each value is a list of integers between 0 and 100
    for values in result.values():
        assert isinstance(values, list)
        assert all(isinstance(x, int) and 0 <= x <= 100 for x in values)
    
    # Check if the dictionary is sorted by the mean of the values in descending order
    means = {k: statistics.mean(v) for k, v in result.items()}
    assert list(sorted(means, key=means.get, reverse=True)) == list(result.keys())

def test_task_func_with_single_letter():
    # Test with a single letter
    letters = ['X']
    result = task_func(letters)
    
    # Check if the result is a dictionary with the correct key
    assert list(result.keys()) == ['X']
    
    # Check if the value is a list of integers between 0 and 100
    values = result['X']
    assert isinstance(values, list)
    assert all(isinstance(x, int) and 0 <= x <= 100 for x in values)

def test_task_func_with_empty_input():
    # Test with an empty input
    letters = []
    result = task_func(letters)
    
    # Check if the result is an empty dictionary
    assert result == {}

def test_task_func_with_repeated_letters():
    # Test with repeated letters
    letters = ['A', 'A', 'B']
    result = task_func(letters)
    
    # Check if the result is a dictionary with unique keys
    assert set(result.keys()) == {'A', 'B'}
    
    # Check if each value is a list of integers between 0 and 100
    for values in result.values():
        assert isinstance(values, list)
        assert all(isinstance(x, int) and 0 <= x <= 100 for x in values)
    
    # Check if the dictionary is sorted by the mean of the values in descending order
    means = {k: statistics.mean(v) for k, v in result.items()}
    assert list(sorted(means, key=means.get, reverse=True)) == list(result.keys())