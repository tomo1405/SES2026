python
import random
from collections import Counter
from statistics import mode
import pytest

def task_func(list_length=1000, range_start=1, range_end=10, random_seed=None):
    random.seed(random_seed)
    random_list = [random.randint(range_start, range_end) for _ in range(list_length)]
    counter = Counter(random_list)
    numbers = ((number, count) for number, count in counter.items())
    return mode(random_list), numbers

def test_task_func():
    # Test with default arguments
    assert task_func() == (None, None)

    # Test with custom arguments
    assert task_func(list_length=5, range_start=1, range_end=10, random_seed=42) == (None, None)

    # Test with list of length 1
    assert task_func(list_length=1, range_start=1, range_end=10, random_seed=42) == (None, None)

    # Test with list of length 1000 and random seed
    assert task_func(list_length=1000, range_start=1, range_end=10, random_seed=42) == (None, None)

    # Test with list of length 1000 and no random seed
    assert task_func(list_length=1000, range_start=1, range_end=10) == (None, None)

    # Test with list of length 1000 and range start/end
    assert task_func(list_length=1000, range_start=1, range_end=10) == (None, None)

    # Test with list of length 1000 and range start/end and random seed
    assert task_func(list_length=1000, range_start=1, range_end=10, random_seed=42) == (None, None)