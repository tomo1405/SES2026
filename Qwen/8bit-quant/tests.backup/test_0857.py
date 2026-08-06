import pytest
from src_0857 import task_func
from itertools import combinations
import numpy as np

def test_task_func_default_parameters():
    sum_of_products, matrix = task_func()
    assert matrix.shape == (3, 3)
    assert 1 <= np.min(matrix) <= 10
    assert 1 <= np.max(matrix) <= 10
    values = matrix.flatten()
    all_pairs = list(combinations(values, 2))
    expected_sum_of_products = sum(np.prod(pair) for pair in all_pairs)
    assert sum_of_products == expected_sum_of_products

def test_task_func_custom_shape():
    sum_of_products, matrix = task_func((4, 4))
    assert matrix.shape == (4, 4)
    assert 1 <= np.min(matrix) <= 10
    assert 1 <= np.max(matrix) <= 10
    values = matrix.flatten()
    all_pairs = list(combinations(values, 2))
    expected_sum_of_products = sum(np.prod(pair) for pair in all_pairs)
    assert sum_of_products == expected_sum_of_products

def test_task_func_custom_range():
    sum_of_products, matrix = task_func(low=5, high=15)
    assert matrix.shape == (3, 3)
    assert 5 <= np.min(matrix) <= 15
    assert 5 <= np.max(matrix) <= 15
    values = matrix.flatten()
    all_pairs = list(combinations(values, 2))
    expected_sum_of_products = sum(np.prod(pair) for pair in all_pairs)
    assert sum_of_products == expected_sum_of_products

def test_task_func_seed():
    sum_of_products_1, matrix_1 = task_func(seed=0)
    sum_of_products_2, matrix_2 = task_func(seed=0)
    assert np.array_equal(matrix_1, matrix_2)
    assert sum_of_products_1 == sum_of_products_2

def test_task_func_invalid_high_low():
    with pytest.raises(ValueError):
        task_func(low=10, high=10)
    with pytest.raises(ValueError):
        task_func(low=10, high=9)