import pytest
from src_0736 import task_func
import numpy as np

def test_task_func_with_positive_numbers():
    L = [[1, 2, 3], [4, 5, 6]]
    result = task_func(L)
    assert np.isclose(result['mean'], 3.5)
    assert np.isclose(result['variance'], 2.9166666666666665)

def test_task_func_with_mixed_numbers():
    L = [[-1, 0, 1], [2, -2, 3]]
    result = task_func(L)
    assert np.isclose(result['mean'], 0.5)
    assert np.isclose(result['variance'], 3.5)

def test_task_func_with_single_element():
    L = [[5]]
    result = task_func(L)
    assert np.isclose(result['mean'], 5.0)
    assert np.isclose(result['variance'], 0.0)

def test_task_func_with_empty_list():
    L = [[]]
    with pytest.raises(ValueError):
        task_func(L)

def test_task_func_with_nested_empty_lists():
    L = [[], []]
    with pytest.raises(ValueError):
        task_func(L)

def test_task_func_with_non_numeric_values():
    L = [[1, 'a', 3], [4, 5, 6]]
    with pytest.raises(TypeError):
        task_func(L)