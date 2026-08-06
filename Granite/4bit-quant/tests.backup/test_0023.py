import collections
from itertools import zip_longest
from random import choices

def task_func(l1, l2, K=10):
    combined = [val for pair in zip_longest(l1, l2) for val in pair if val is not None]
    sample = choices(combined, k=K)
    freq = collections.Counter(sample)
    return freq

def test_task_func():
    l1 = [1, 2, 3]
    l2 = [4, 5, 6]
    K = 5
    expected_combined = [1, 2, 3, 4, 5, 6]
    expected_sample = choices(expected_combined, k=K)
    expected_freq = collections.Counter(expected_sample)
    actual_freq = task_func(l1, l2, K)
    assert actual_freq == expected_freq