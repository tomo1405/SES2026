import pytest
from functools import reduce
from itertools import combinations
import numpy as np

def task_func(shape=(3, 3), low=1, high=10, seed=None):
    if seed is not None:
        np.random.seed(seed)

    if high <= low:
        raise ValueError("The 'high' parameter must be greater than 'low'.")

    matrix = np.random.randint(low, high, shape)
    values = matrix.flatten()

    all_pairs = list(combinations(values, 2))

    sum_of_products = reduce(lambda a, b: a + b, [np.prod(pair) for pair in all_pairs])

    return sum_of_products, matrix

def test_task_func():
    # Test case 1: Default parameters
    result = task_func()
    expected_sum_of_products = 1116
    expected_matrix = np.array([[8, 1, 6], [10, 3, 7], [10, 9, 10]])
    assert result[0] == expected_sum_of_products
    assert np.array_equal(result[1], expected_matrix)

    # Test case 2: Custom parameters
    result = task_func(shape=(2, 2), low=1, high=10, seed=42)
    expected_sum_of_products = 1116
    expected_matrix = np.array([[8, 1], [10, 3]])
    assert result[0] == expected_sum_of_products
    assert np.array_equal(result[1], expected_matrix)

    # Test case 3: Invalid parameters
    with pytest.raises(ValueError):
        task_func(shape=(3, 3), low=10, high=1, seed=None)