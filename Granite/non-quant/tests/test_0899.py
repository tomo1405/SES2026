import pytest
from src_0899 import task_func
from collections import Counter
import random

LETTERS = ['a', 'b', 'c', 'd', 'e']

def test_task_func():
    # Test case 1: count = 5, seed = 0
    count = 5
    seed = 0
    random.seed(seed)
    pairs = [tuple(random.choices(LETTERS, k=2)) for _ in range(count)]
    expected_pair_frequency = Counter(pairs)
    actual_pair_frequency = task_func(count, seed)
    assert actual_pair_frequency == expected_pair_frequency

    # Test case 2: count = 10, seed = 1
    count = 10
    seed = 1
    random.seed(seed)
    pairs = [tuple(random.choices(LETTERS, k=2)) for _ in range(count)]
    expected_pair_frequency = Counter(pairs)
    actual_pair_frequency = task_func(count, seed)
    assert actual_pair_frequency == expected_pair_frequency

    # Test case 3: count = 15, seed = 2
    count = 15
    seed = 2
    random.seed(seed)
    pairs = [tuple(random.choices(LETTERS, k=2)) for _ in range(count)]
    expected_pair_frequency = Counter(pairs)
    actual_pair_frequency = task_func(count, seed)
    assert actual_pair_frequency == expected_pair_frequency