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
    list_of_tuples = [(1, 'A'), (2, 'B'), (3, 'A'), (4, 'C'), (5, 'B')]
    total_sum, category_counts = task_func(list_of_tuples)
    assert total_sum == 15
    assert category_counts == {'A': 2, 'B': 2, 'C': 1}