import pytest
from src_0003 import task_func
import random
import statistics

def test_task_func():
    # Test with a small set of letters
    letters = ['A', 'B', 'C']
    result = task_func(letters)
    
    # Check if the result is a dictionary
    assert isinstance(result, dict)
    
    # Check if all keys from the input are present in the result
    assert set(result.keys()) == set(letters)
    
    # Check if each value is a list of integers between 0 and 100
    for values in result.values():
        assert isinstance(values, list)
        assert all(isinstance(x, int) and 0 <= x <= 100 for x in values)
    
    # Check if the dictionary is sorted by the mean of the lists in descending order
    means = {k: statistics.mean(v) for k, v in result.items()}
    sorted_means = dict(sorted(means.items(), key=lambda item: item[1], reverse=True))
    assert means == sorted_means

def test_task_func_empty_input():
    # Test with an empty list of letters
    letters = []
    result = task_func(letters)
    
    # Check if the result is an empty dictionary
    assert result == {}

def test_task_func_single_letter():
    # Test with a single letter
    letters = ['X']
    result = task_func(letters)
    
    # Check if the result is a dictionary with the single letter as the key
    assert result == {'X': [random.randint(0, 100) for _ in range(random.randint(1, 10))]}