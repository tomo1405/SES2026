import pytest
from src_0752 import task_func

def test_task_func_with_uniform_weights():
    values = [1, 2, 3]
    weights = [1, 1, 1]
    n_samples = 10
    result = task_func(values, weights, n_samples)
    assert len(result) == 3
    for value in values:
        assert value in result
        assert isinstance(result[value], int)

def test_task_func_with_non_uniform_weights():
    values = ['a', 'b', 'c']
    weights = [1, 2, 3]
    n_samples = 10
    result = task_func(values, weights, n_samples)
    assert len(result) == 3
    for value in values:
        assert value in result
        assert isinstance(result[value], int)
    assert result['c'] > result['b'] > result['a']

def test_task_func_with_single_value():
    values = [42]
    weights = [1]
    n_samples = 5
    result = task_func(values, weights, n_samples)
    assert len(result) == 1
    assert 42 in result
    assert result[42] == 5

def test_task_func_with_zero_samples():
    values = [1, 2, 3]
    weights = [1, 1, 1]
    n_samples = 0
    result = task_func(values, weights, n_samples)
    assert result == {}

def test_task_func_with_negative_samples():
    values = [1, 2, 3]
    weights = [1, 1, 1]
    n_samples = -1
    with pytest.raises(ValueError):
        task_func(values, weights, n_samples)

def test_task_func_with_empty_values():
    values = []
    weights = []
    n_samples = 5
    result = task_func(values, weights, n_samples)
    assert result == {}

def test_task_func_with_mismatched_lengths():
    values = [1, 2]
    weights = [1, 1, 1]
    n_samples = 5
    with pytest.raises(ValueError):
        task_func(values, weights, n_samples)