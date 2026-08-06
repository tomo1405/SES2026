import pytest
from src_0752 import task_func

def test_task_func():
    values = ['a', 'b', 'c']
    weights = [1, 2, 3]
    n_samples = 10
    
    result = task_func(values, weights, n_samples)
    
    # Check that the result is a dictionary
    assert isinstance(result, dict)
    
    # Check that all keys in result are in values
    assert set(result.keys()).issubset(set(values))
    
    # Check that the sum of the values in the result is equal to n_samples
    assert sum(result.values()) == n_samples
    
    # Check that the weights are respected (basic check, not exhaustive)
    # The probability of 'c' should be higher than 'b', and 'b' higher than 'a'
    assert result.get('c', 0) >= result.get('b', 0) >= result.get('a', 0)

def test_task_func_empty_values():
    values = []
    weights = []
    n_samples = 10
    
    result = task_func(values, weights, n_samples)
    
    # Check that the result is an empty dictionary
    assert result == {}

def test_task_func_single_value():
    values = ['x']
    weights = [1]
    n_samples = 10
    
    result = task_func(values, weights, n_samples)
    
    # Check that the result is a dictionary with the correct value
    assert result == {'x': n_samples}

def test_task_func_zero_samples():
    values = ['a', 'b', 'c']
    weights = [1, 2, 3]
    n_samples = 0
    
    result = task_func(values, weights, n_samples)
    
    # Check that the result is an empty dictionary
    assert result == {}