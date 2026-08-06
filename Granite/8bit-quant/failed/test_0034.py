import numpy as np
from functools import reduce
from src_0034 import task_func

def test_task_func():
    list_of_pairs = [(1, 2), (3, 4), (5, 6)]
    expected_product = reduce(lambda x, y: x * y, [pair[1] for pair in list_of_pairs])
    expected_product_array = np.array([expected_product])

    actual_product_array = task_func(list_of_pairs)

    assert np.array_equal(actual_product_array, expected_product_array)

def test_task_func_with_empty_list():
    list_of_pairs = []
    expected_product_array = np.array([1])

    actual_product_array = task_func(list_of_pairs)

    assert np.array_equal(actual_product_array, expected_product_array)

def test_task_func_with_one_pair():
    list_of_pairs = [(7, 8)]
    expected_product_array = np.array([8])

    actual_product_array = task_func(list_of_pairs)

    assert np.array_equal(actual_product_array, expected_product_array)