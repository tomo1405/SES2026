python
import itertools
import math
import pandas as pd
import pytest

from src_0300 import task_func

def test_task_func():
    # Test case 1: subset_size > len(elements)
    elements = [1, 2, 3]
    subset_size = 4
    top_n = 2
    expected_product = 1
    expected_top_sums = pd.Series([])
    actual_product, actual_top_sums = task_func(elements, subset_size, top_n)
    assert actual_product == expected_product
    assert actual_top_sums.equals(expected_top_sums)

    # Test case 2: subset_size <= 0
    elements = [1, 2, 3]
    subset_size = 0
    top_n = 2
    expected_product = 1
    expected_top_sums = pd.Series([])
    actual_product, actual_top_sums = task_func(elements, subset_size, top_n)
    assert actual_product == expected_product
    assert actual_top_sums.equals(expected_top_sums)

    # Test case 3: subset_size is valid and top_n is valid
    elements = [1, 2, 3, 4, 5]
    subset_size = 2
    top_n = 3
    expected_product = 10
    expected_top_sums = pd.Series([9, 7, 5])
    actual_product, actual_top_sums = task_func(elements, subset_size, top_n)
    assert actual_product == expected_product
    assert actual_top_sums.equals(expected_top_sums)

    # Test case 4: subset_size is valid and top_n is invalid
    elements = [1, 2, 3, 4, 5]
    subset_size = 2
    top_n = 0
    expected_product = 10
    expected_top_sums = pd.Series([])
    actual_product, actual_top_sums = task_func(elements, subset_size, top_n)
    assert actual_product == expected_product
    assert actual_top_sums.equals(expected_top_sums)

    # Test case 5: subset_size is invalid and top_n is valid
    elements = [1, 2, 3, 4, 5]
    subset_size = 0
    top_n = 3
    expected_product = 1
    expected_top_sums = pd.Series([])
    actual_product, actual_top_sums = task_func(elements, subset_size, top_n)
    assert actual_product == expected_product
    assert actual_top_sums.equals(expected_top_sums)

    # Test case 6: subset_size is invalid and top_n is invalid
    elements = [1, 2, 3, 4, 5]
    subset_size = 0
    top_n = 0
    expected_product = 1
    expected_top_sums = pd.Series([])
    actual_product, actual_top_sums = task_func(elements, subset_size, top_n)
    assert actual_product == expected_product
    assert actual_top_sums.equals(expected_top_sums)