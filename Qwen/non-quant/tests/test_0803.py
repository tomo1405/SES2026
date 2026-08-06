import itertools

import numpy as np
import pytest
from src_0803 import task_func


def test_task_func_dimension_zero():
    with pytest.raises(ValueError):
        task_func(0)

def test_task_func_negative_dimension():
    with pytest.raises(ValueError):
        task_func(-5)

def test_task_func_dimension_one():
    matrix, flat_list = task_func(1)
    assert isinstance(matrix, np.ndarray)
    assert matrix.shape == (1, 1)
    assert isinstance(flat_list, list)
    assert len(flat_list) == 1
    assert 1 <= flat_list[0] <= 100

def test_task_func_dimension_two():
    matrix, flat_list = task_func(2)
    assert isinstance(matrix, np.ndarray)
    assert matrix.shape == (2, 2)
    assert isinstance(flat_list, list)
    assert len(flat_list) == 4
    for value in flat_list:
        assert 1 <= value <= 100

def test_task_func_reproducibility():
    matrix1, _ = task_func(3)
    matrix2, _ = task_func(3)
    assert np.array_equal(matrix1, matrix2)

def test_task_func_combinations():
    _, flat_list = task_func(2)
    combinations = list(itertools.combinations(flat_list, 2))
    assert len(combinations) == 6  # C(4, 2) = 6

def test_task_func_large_dimension():
    matrix, flat_list = task_func(10)
    assert isinstance(matrix, np.ndarray)
    assert matrix.shape == (10, 10)
    assert isinstance(flat_list, list)
    assert len(flat_list) == 100
    for value in flat_list:
        assert 1 <= value <= 100