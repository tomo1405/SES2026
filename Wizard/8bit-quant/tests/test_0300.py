python
import itertools
import math
from pandas import Series

def task_func(elements, subset_size, top_n=2):
    if subset_size > len(elements) or subset_size <= 0:
        return 1, []

    combinations = list(itertools.combinations(elements, subset_size))
    sums = [sum(combination) for combination in combinations if len(combination) != 0]
    product = math.prod(sums)
    top_sums = sorted(sums, reverse=True)[:top_n]
    top_sums = Series(top_sums)
    return product, top_sums

def test_task_func():
    # Test case 1
    elements = [1, 2, 3, 4, 5]
    subset_size = 2
    top_n = 2
    expected_product = 10
    expected_top_sums = [10, 9]
    actual_product, actual_top_sums = task_func(elements, subset_size, top_n)
    assert actual_product == expected_product
    assert actual_top_sums.tolist() == expected_top_sums

    # Test case 2
    elements = [1, 2, 3, 4, 5]
    subset_size = 3
    top_n = 2
    expected_product = 60
    expected_top_sums = [15, 10]
    actual_product, actual_top_sums = task_func(elements, subset_size, top_n)
    assert actual_product == expected_product
    assert actual_top_sums.tolist() == expected_top_sums

    # Test case 3
    elements = [1, 2, 3, 4, 5]
    subset_size = 4
    top_n = 2
    expected_product = 24
    expected_top_sums = [12, 8]
    actual_product, actual_top_sums = task_func(elements, subset_size, top_n)
    assert actual_product == expected_product
    assert actual_top_sums.tolist() == expected_top_sums

    # Test case 4
    elements = [1, 2, 3, 4, 5]
    subset_size = 5
    top_n = 2
    expected_product = 120
    expected_top_sums = [15, 10]
    actual_product, actual_top_sums = task_func(elements, subset_size, top_n)
    assert actual_product == expected_product
    assert actual_top_sums.tolist() == expected_top_sums

    # Test case 5
    elements = [1, 2, 3, 4, 5]
    subset_size = 6
    top_n = 2
    expected_product = 720
    expected_top_sums = [15, 10]
    actual_product, actual_top_sums = task_func(elements, subset_size, top_n)
    assert actual_product == expected_product
    assert actual_top_sums.tolist() == expected_top_sums

    # Test case 6
    elements = [1, 2, 3, 4, 5]
    subset_size = 1
    top_n = 2
    expected_product = 1
    expected_top_sums = [1, 1]
    actual_product, actual_top_sums = task_func(elements, subset_size, top_n)
    assert actual_product == expected_product
    assert actual_top_sums.tolist() == expected_top_sums

    # Test case 7
    elements = [1, 2, 3, 4, 5]
    subset_size = 0
    top_n = 2
    expected_product = 1
    expected_top_sums = []
    actual_product, actual_top_sums = task_func(elements, subset_size, top_n)
    assert actual_product == expected_product
    assert actual_top_sums.tolist() == expected_top_sums

    # Test case 8
    elements = [1, 2, 3, 4, 5]
    subset_size = 7
    top_n = 2
    expected_product = 1
    expected_top_sums = []
    actual_product, actual_top_sums = task_func(elements, subset_size, top_n)
    assert actual_product == expected_product
    assert actual_top_sums.tolist() == expected_top_sums

    # Test case 9
    elements = [1, 2, 3, 4, 5]
    subset_size = 2
    top_n = 3
    expected_product = 10
    expected_top_sums = [10, 9, 8]
    actual_product, actual_top_sums = task_func(elements, subset_size, top_n)
    assert actual_product == expected_product
    assert actual_top_sums.tolist() == expected_top_sums

    # Test case 10
    elements = [1, 2, 3, 4, 5]
    subset_size = 3
    top_n = 3
    expected_product = 60
    expected_top_sums = [15, 10, 5]
    actual_product, actual_top_sums = task_func(elements, subset_size, top_n)
    assert actual_product == expected_product
    assert actual_top_sums.tolist() == expected_top_sums

    # Test case 11
    elements = [1, 2, 3, 4, 5]
    subset_size = 4
    top_n = 3
    expected_product = 24
    expected_top_sums = [12, 8, 4]
    actual_product, actual_top_sums = task_func(elements, subset_size, top_n)
    assert actual_product == expected_product
    assert actual_top_sums.tolist() == expected_top_sums

    # Test case 12
    elements = [1, 2, 3, 4, 5]
    subset_size = 5
    top_n = 3
    expected_product = 120
    expected_top_sums = [15, 10, 5]
    actual_product, actual_top_sums = task_func(elements, subset_size, top_n)
    assert actual_product == expected_product
    assert actual_top_sums.tolist() == expected_top_sums

    # Test case 13
    elements = [1, 2, 3, 4, 5]
    subset_size = 6
    top_n = 3
    expected_product = 720
    expected_top_sums = [15, 10, 5]
    actual_product, actual_top_sums = task_func(elements, subset_size, top_n)
    assert actual_product == expected_product
    assert actual_top_sums.tolist() == expected_top_sums

    # Test case 14
    elements = [1, 2, 3, 4, 5]
    subset_size = 1
    top_n = 3
    expected_product = 1
    expected_top_sums = [1, 1, 1]
    actual_product, actual_top_sums = task_func(elements, subset_size, top_n)
    assert actual_product == expected_product
    assert actual_top_sums.tolist() == expected_top_sums

    # Test case 15
    elements = [1, 2, 3, 4, 5]
    subset_size = 0
    top_n = 3
    expected_product = 1
    expected_top_sums = []
    actual_product, actual_top_sums = task_func(elements, subset_size, top_n)
    assert actual_product == expected_product
    assert actual_top_sums.tolist() == expected_top_sums

    # Test case 16
    elements = [1, 2, 3, 4, 5]
    subset_size = 7
    top_n = 3
    expected_product = 1
    expected_top_sums = []
    actual_product, actual_top_sums = task_func(elements, subset_size, top_n)
    assert actual_product == expected_product
    assert actual_top_sums.tolist() == expected_top_sums