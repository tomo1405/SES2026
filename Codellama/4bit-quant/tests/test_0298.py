import collections
import itertools

from src_0298 import task_func


def test_task_func():
    elements = [1, 2, 3, 4, 5]
    subset_size = 2
    combinations = list(itertools.combinations(elements, subset_size))
    sums = [sum(combination) for combination in combinations]
    expected_result = collections.Counter(sums)

    result = task_func(elements, subset_size)

    assert result == expected_result