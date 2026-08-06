import pytest
from src_0116 import task_func
import numpy as np
from scipy.stats import mode, entropy

def test_task_func_with_positive_numbers():
    numbers = [1, 2, 2, 3, 3, 3, 4]
    result = task_func(numbers)
    assert 'array' in result
    assert 'mode' in result
    assert 'entropy' in result
    np.testing.assert_array_equal(result['array'], np.array(numbers))
    assert result['mode'] == 3
    assert np.isclose(result['entropy'], entropy(np.array(numbers), base=2))

def test_task_func_with_single_number():
    numbers = [5]
    result = task_func(numbers)
    assert 'array' in result
    assert 'mode' in result
    assert 'entropy' in result
    np.testing.assert_array_equal(result['array'], np.array(numbers))
    assert result['mode'] == 5
    assert np.isclose(result['entropy'], entropy(np.array(numbers), base=2))

def test_task_func_with_negative_numbers():
    numbers = [-1, -2, -2, -3, -3, -3, -4]
    result = task_func(numbers)
    assert 'array' in result
    assert 'mode' in result
    assert 'entropy' in result
    np.testing.assert_array_equal(result['array'], np.array(numbers))
    assert result['mode'] == -3
    assert np.isclose(result['entropy'], entropy(np.array(numbers), base=2))

def test_task_func_with_zero():
    numbers = [0, 0, 0, 1, 1, 2]
    result = task_func(numbers)
    assert 'array' in result
    assert 'mode' in result
    assert 'entropy' in result
    np.testing.assert_array_equal(result['array'], np.array(numbers))
    assert result['mode'] == 0
    assert np.isclose(result['entropy'], entropy(np.array(numbers), base=2))

def test_task_func_with_empty_list():
    with pytest.raises(ValueError):
        task_func([])