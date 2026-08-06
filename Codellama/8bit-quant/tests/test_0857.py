import numpy as np
from src_0857 import task_func


def test_task_func_shape():
    shape = (3, 3)
    low = 1
    high = 10
    seed = None
    expected_shape = (3, 3)

    result, matrix = task_func(shape, low, high, seed)

    assert matrix.shape == expected_shape

def test_task_func_low():
    shape = (3, 3)
    low = 1
    high = 10
    seed = None
    expected_low = 1

    result, matrix = task_func(shape, low, high, seed)

    assert np.min(matrix) == expected_low

def test_task_func_high():
    shape = (3, 3)
    low = 1
    high = 10
    seed = None
    expected_high = 10

    result, matrix = task_func(shape, low, high, seed)

    assert np.max(matrix) == expected_high

def test_task_func_seed():
    shape = (3, 3)
    low = 1
    high = 10
    seed = 42
    expected_seed = 42

    result, matrix = task_func(shape, low, high, seed)

    assert np.random.get_state()[1][0] == expected_seed

def test_task_func_sum_of_products():
    shape = (3, 3)
    low = 1
    high = 10
    seed = None
    expected_sum_of_products = 100

    result, matrix = task_func(shape, low, high, seed)

    assert result == expected_sum_of_products