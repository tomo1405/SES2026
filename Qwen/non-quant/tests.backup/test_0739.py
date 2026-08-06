import pytest
from src_0739 import task_func
import numpy as np
from scipy.stats import iqr

def test_task_func_with_integers():
    L = [[1, 2, 3], [4, 5, 6]]
    expected_iqr = iqr(np.array([1, 2, 3, 4, 5, 6]).flatten())
    assert np.isclose(task_func(L), expected_iqr)

def test_task_func_with_floats():
    L = [[1.5, 2.5, 3.5], [4.5, 5.5, 6.5]]
    expected_iqr = iqr(np.array([1.5, 2.5, 3.5, 4.5, 5.5, 6.5]).flatten())
    assert np.isclose(task_func(L), expected_iqr)

def test_task_func_with_mixed_integers_and_floats():
    L = [[1, 2.5, 3], [4, 5.5, 6]]
    expected_iqr = iqr(np.array([1, 2.5, 3, 4, 5.5, 6]).flatten())
    assert np.isclose(task_func(L), expected_iqr)

def test_task_func_with_single_element():
    L = [[7]]
    expected_iqr = iqr(np.array([7]).flatten())
    assert np.isclose(task_func(L), expected_iqr)

def test_task_func_with_empty_list():
    L = [[]]
    with pytest.raises(ValueError):
        task_func(L)

def test_task_func_with_nested_empty_lists():
    L = [[], []]
    with pytest.raises(ValueError):
        task_func(L)

def test_task_func_with_large_numbers():
    L = [[1e6, 2e6, 3e6], [4e6, 5e6, 6e6]]
    expected_iqr = iqr(np.array([1e6, 2e6, 3e6, 4e6, 5e6, 6e6]).flatten())
    assert np.isclose(task_func(L), expected_iqr)

def test_task_func_with_negative_numbers():
    L = [[-1, -2, -3], [-4, -5, -6]]
    expected_iqr = iqr(np.array([-1, -2, -3, -4, -5, -6]).flatten())
    assert np.isclose(task_func(L), expected_iqr)