import pytest
from src_0694 import task_func
import numpy as np

def test_task_func_with_positive_values():
    tuples_list = [(1, 2), (3, 4), (5, 6)]
    columns = ['A', 'B']
    result = task_func(tuples_list, columns)
    expected_mean = np.zeros(2)
    expected_std = np.ones(2)
    assert np.allclose(result.mean(), expected_mean)
    assert np.allclose(result.std(), expected_std)

def test_task_func_with_negative_values():
    tuples_list = [(-1, -2), (-3, -4), (-5, -6)]
    columns = ['A', 'B']
    result = task_func(tuples_list, columns)
    expected_mean = np.zeros(2)
    expected_std = np.ones(2)
    assert np.allclose(result.mean(), expected_mean)
    assert np.allclose(result.std(), expected_std)

def test_task_func_with_mixed_values():
    tuples_list = [(1, -2), (3, 4), (-5, 6)]
    columns = ['A', 'B']
    result = task_func(tuples_list, columns)
    expected_mean = np.zeros(2)
    expected_std = np.ones(2)
    assert np.allclose(result.mean(), expected_mean)
    assert np.allclose(result.std(), expected_std)

def test_task_func_with_single_element():
    tuples_list = [(1,)]
    columns = ['A']
    result = task_func(tuples_list, columns)
    expected_mean = np.array([0])
    expected_std = np.array([1])
    assert np.allclose(result.mean(), expected_mean)
    assert np.allclose(result.std(), expected_std)

def test_task_func_with_empty_list():
    tuples_list = []
    columns = ['A', 'B']
    with pytest.raises(ValueError):
        task_func(tuples_list, columns)

def test_task_func_with_different_length_tuples():
    tuples_list = [(1, 2), (3, 4), (5,)]
    columns = ['A', 'B']
    with pytest.raises(ValueError):
        task_func(tuples_list, columns)

def test_task_func_with_non_numeric_data():
    tuples_list = [('a', 'b'), ('c', 'd'), ('e', 'f')]
    columns = ['A', 'B']
    with pytest.raises(ValueError):
        task_func(tuples_list, columns)