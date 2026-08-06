import pytest
from functools import reduce
import numpy as np

def task_func(list_of_pairs):
    second_values = [pair[1] for pair in list_of_pairs]
    product = reduce(np.multiply, second_values)
    product_array = np.array([product])

    return product_array

def test_task_func():
    list_of_pairs = [(1, 2), (3, 4), (5, 6)]
    expected_output = np.array([np.multiply(*pair) for pair in list_of_pairs])

    actual_output = task_func(list_of_pairs)

    assert np.array_equal(actual_output, expected_output)