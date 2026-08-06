import pytest
from src_0116 import task_func
import numpy as np
from scipy.stats import mode, entropy

def test_task_func_with_non_empty_list():
    numbers = [1, 2, 2, 3, 4]
    result = task_func(numbers)
    assert isinstance(result, dict)
    assert 'array' in result
    assert 'mode' in result
    assert 'entropy' in result
    assert np.array_equal(result['array'], numbers)
    assert result['mode'] == 2
    assert np.isclose(result['entropy'], entropy(numbers, base=2))

def test_task_func_with_single_element():
    numbers = [5]
    result = task_func(numbers)
    assert isinstance(result, dict)
    assert 'array' in result
    assert 'mode' in result
    assert 'entropy' in result
    assert np.array_equal(result['array'], numbers)
    assert result['mode'] == 5
    assert np.isclose(result['entropy'], entropy([1], base=2))

def test_task_func_with_all_same_elements():
    numbers = [7, 7, 7, 7]
    result = task_func(numbers)
    assert isinstance(result, dict)
    assert 'array' in result
    assert 'mode' in result
    assert 'entropy' in result
    assert np.array_equal(result['array'], numbers)
    assert result['mode'] == 7
    assert np.isclose(result['entropy'], 0)

def test_task_func_with_zero_length_list():
    with pytest.raises(ValueError):
        task_func([])