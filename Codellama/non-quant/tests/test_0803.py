import itertools

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

def test_task_func_seed():
    dimension = 5
    seed = 42
    matrix1, flat_list1 = task_func(dimension, seed)
    matrix2, flat_list2 = task_func(dimension, seed)
    assert np.array_equal(matrix1, matrix2)
    assert flat_list1 == flat_list2

def test_task_func_combinations():
    dimension = 5
    matrix, flat_list = task_func(dimension)
    combinations = list(itertools.combinations(flat_list, 2))
    assert len(combinations) == (dimension * (dimension - 1)) // 2
    for combination in combinations:
        assert len(combination) == 2
        assert combination[0] < combination[1]