from typing import Counter

from src_0899 import task_func


def test_task_func():
    count = 10
    seed = 0
    pairs = [('a', 'b'), ('c', 'd'), ('e', 'a'), ('b', 'c'), ('d', 'e')]
    pair_frequency = Counter(pairs)

    assert task_func(count, seed) == pair_frequency

def test_task_func_with_different_seed():
    count = 10
    seed = 1
    pairs = [('a', 'b'), ('c', 'd'), ('e', 'a'), ('b', 'c'), ('d', 'e')]
    pair_frequency = Counter(pairs)

    assert task_func(count, seed) == pair_frequency

def test_task_func_with_different_count():
    count = 20
    seed = 0
    pairs = [('a', 'b'), ('c', 'd'), ('e', 'a'), ('b', 'c'), ('d', 'e')]
    pair_frequency = Counter(pairs)

    assert task_func(count, seed) == pair_frequency