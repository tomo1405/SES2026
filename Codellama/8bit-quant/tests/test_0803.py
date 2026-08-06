import numpy as np
import pytest
from src_0803 import task_func


def test_task_func_positive_dimension():
    dimension = 5
    matrix, flat_list = task_func(dimension)
    assert matrix.shape == (dimension, dimension)
    assert len(flat_list) == dimension * dimension

def test_task_func_negative_dimension():
    dimension = -1
    with pytest.raises(ValueError):
        task_func(dimension)

def test_task_func_zero_dimension():
    dimension = 0
    with pytest.raises(ValueError):
        task_func(dimension)

def test_task_func_non_integer_dimension():
    dimension = 5.5
    with pytest.raises(ValueError):
        task_func(dimension)

def test_task_func_seed():
    dimension = 5
    seed = 42
    matrix, flat_list = task_func(dimension, seed)
    assert matrix.shape == (dimension, dimension)
    assert len(flat_list) == dimension * dimension
    assert np.random.get_state()[1][0] == seed