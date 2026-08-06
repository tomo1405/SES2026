import pytest
from src_0857 import task_func

def test_task_func_shape():
    shape = (3, 3)
    low = 1
    high = 10
    seed = None
    sum_of_products, matrix = task_func(shape, low, high, seed)
    assert matrix.shape == shape

def test_task_func_low():
    shape = (3, 3)
    low = 1
    high = 10
    seed = None
    sum_of_products, matrix = task_func(shape, low, high, seed)
    assert np.min(matrix) >= low

def test_task_func_high():
    shape = (3, 3)
    low = 1
    high = 10
    seed = None
    sum_of_products, matrix = task_func(shape, low, high, seed)
    assert np.max(matrix) < high

def test_task_func_seed():
    shape = (3, 3)
    low = 1
    high = 10
    seed = 1234
    sum_of_products, matrix = task_func(shape, low, high, seed)
    assert np.allclose(matrix, np.random.RandomState(seed).randint(low, high, shape))

def test_task_func_sum_of_products():
    shape = (3, 3)
    low = 1
    high = 10
    seed = None
    sum_of_products, matrix = task_func(shape, low, high, seed)
    all_pairs = list(combinations(matrix.flatten(), 2))
    expected_sum_of_products = reduce(lambda a, b: a + b, [np.prod(pair) for pair in all_pairs])
    assert sum_of_products == expected_sum_of_products