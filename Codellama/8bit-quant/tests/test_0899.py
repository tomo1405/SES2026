from typing import Counter

from src_0899 import task_func


def test_task_func():
    count = 10
    seed = 0
    pairs = [('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'e'), ('e', 'a')]
    pair_frequency = Counter(pairs)

    assert task_func(count, seed) == pair_frequency