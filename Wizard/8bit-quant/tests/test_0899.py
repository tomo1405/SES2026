python
import random
from collections import Counter

LETTERS = ['a', 'b', 'c', 'd', 'e']

def task_func(count, seed=0):
    random.seed(seed)

    pairs = [tuple(random.choices(LETTERS, k=2)) for _ in range(count)]
    pair_frequency = Counter(pairs)

    return pair_frequency

def test_task_func():
    # Test case 1
    assert task_func(10, seed=42) == Counter({('a', 'b'): 2, ('a', 'c'): 1, ('a', 'd'): 1, ('a', 'e'): 1, ('b', 'c'): 1, ('b', 'd'): 1, ('b', 'e'): 1, ('c', 'd'): 1, ('c', 'e'): 1, ('d', 'e'): 1})

    # Test case 2
    assert task_func(0, seed=42) == Counter()

    # Test case 3
    assert task_func(10, seed=0) != Counter({('a', 'b'): 2, ('a', 'c'): 1, ('a', 'd'): 1, ('a', 'e'): 1, ('b', 'c'): 1, ('b', 'd'): 1, ('b', 'e'): 1, ('c', 'd'): 1, ('c', 'e'): 1, ('d', 'e'): 1})