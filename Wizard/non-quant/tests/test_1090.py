python
import numpy as np
from collections import Counter
import pytest

def task_func(list_of_tuples):

    numeric_values = [pair[0] for pair in list_of_tuples]
    categories = [pair[1] for pair in list_of_tuples]

    total_sum = np.sum(numeric_values)
    category_counts = Counter(categories)

    return total_sum, dict(category_counts)

def test_task_func():
    list_of_tuples = [(1, 'a'), (2, 'b'), (3, 'a'), (4, 'c')]
    expected_total_sum = 10
    expected_category_counts = {'a': 2, 'b': 1, 'c': 1}

    total_sum, category_counts = task_func(list_of_tuples)

    assert total_sum == expected_total_sum
    assert category_counts == expected_category_counts