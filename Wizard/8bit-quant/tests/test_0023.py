python
import collections
from itertools import zip_longest
from random import choices
import pytest

def task_func(l1, l2, K=10):
    combined = [val for pair in zip_longest(l1, l2) for val in pair if val is not None]
    sample = choices(combined, k=K)
    freq = collections.Counter(sample)
    return freq

def test_task_func():
    l1 = [1, 2, 3]
    l2 = [4, 5, 6]
    K = 2
    expected_freq = {1: 1, 2: 1}
    assert task_func(l1, l2, K) == expected_freq