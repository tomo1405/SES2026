import pytest
from src_0116 import task_func
import numpy as np
from scipy.stats import mode, entropy

def test_task_func_with_valid_input():
    numbers = [1, 2, 2, 3, 3, 3, 4]
    result = task_func(numbers)
    assert isinstance(result, dict)
    assert 'array' in result
    assert np.array_equal(result['array'], np.array(numbers))
    assert 'mode' in result
    assert result['mode'] == 3
    assert 'entropy' in result
    expected_entropy = entropy(np.array([1/7, 2/7, 3/7, 1/7]), base=2)
    assert np.isclose(result['entropy'], expected_entropy)

def test_task_func_with_single_element():
    numbers = [42]
    result = task_func(numbers)
    assert isinstance(result, dict)
    assert 'array' in result
    assert np.array_equal(result['array'], np.array(numbers))
    assert 'mode' in result
    assert result['mode'] == 42
    assert 'entropy' in result
    expected_entropy = entropy(np.array([1]), base=2)
    assert np.isclose(result['entropy'], expected_entropy)

def test_task_func_with_empty_list():
    with pytest.raises(ValueError):
        task_func([])

def test_task_func_with_all_identical_elements():
    numbers = [5, 5, 5, 5]
    result = task_func(numbers)
    assert isinstance(result, dict)
    assert 'array' in result
    assert np.array_equal(result['array'], np.array(numbers))
    assert 'mode' in result
    assert result['mode'] == 5
    assert 'entropy' in result
    expected_entropy = entropy(np.array([1]), base=2)
    assert np.isclose(result['entropy'], expected_entropy)

def test_task_func_with_negative_numbers():
    numbers = [-1, -2, -2, -3, -3, -3, -4]
    result = task_func(numbers)
    assert isinstance(result, dict)
    assert 'array' in result
    assert np.array_equal(result['array'], np.array(numbers))
    assert 'mode' in result
    assert result['mode'] == -3
    assert 'entropy' in result
    expected_entropy = entropy(np.array([1/7, 2/7, 3/7, 1/7]), base=2)
    assert np.isclose(result['entropy'], expected_entropy)