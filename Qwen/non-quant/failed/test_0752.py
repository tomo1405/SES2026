import pytest
from src_0752 import task_func
from collections import Counter

def test_task_func_with_uniform_weights():
    values = [1, 2, 3]
    weights = [1, 1, 1]
    n_samples = 100
    result = task_func(values, weights, n_samples)
    
    # Since weights are uniform, each value should appear approximately the same number of times
    assert len(result) == len(values)
    for count in result.values():
        assert count >= 30 and count <= 40  # Allow some variance

def test_task_func_with_non_uniform_weights():
    values = ['a', 'b', 'c']
    weights = [1, 2, 3]
    n_samples = 1000
    result = task_func(values, weights, n_samples)
    
    # 'c' should appear more often than 'a' and 'b'
    assert result['c'] > result['b'] > result['a']

def test_task_func_with_single_value():
    values = [42]
    weights = [1]
    n_samples = 50
    result = task_func(values, weights, n_samples)
    
    # All samples should be the same value
    assert result == {42: 50}

def test_task_func_with_zero_samples():
    values = [1, 2, 3]
    weights = [1, 1, 1]
    n_samples = 0
    result = task_func(values, weights, n_samples)
    
    # No samples should be returned
    assert result == {}

def test_task_func_with_negative_samples():
    values = [1, 2, 3]
    weights = [1, 1, 1]
    n_samples = -10
    with pytest.raises(ValueError):
        task_func(values, weights, n_samples)

def test_task_func_with_empty_values():
    values = []
    weights = []
    n_samples = 10
    with pytest.raises(ValueError):
        task_func(values, weights, n_samples)

def test_task_func_with_mismatched_lengths():
    values = [1, 2, 3]
    weights = [1, 1]  # Mismatched length
    n_samples = 10
    with pytest.raises(ValueError):
        task_func(values, weights, n_samples)