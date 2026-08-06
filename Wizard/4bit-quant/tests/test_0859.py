python
import string
import random
from collections import Counter

def task_func(n, seed=None):
    LETTERS = string.ascii_lowercase
    if seed is not None:
        random.seed(seed)
    letters = [random.choice(LETTERS) for _ in range(n)]
    letter_counts = Counter(letters)
    return letter_counts

def test_task_func():
    # Test case 1
    assert task_func(5) == {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1}

    # Test case 2
    assert task_func(5, 123) == {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1}

    # Test case 3
    assert task_func(10) == {'a': 2, 'b': 2, 'c': 2, 'd': 2, 'e': 2, 'f': 1, 'g': 1, 'h': 1, 'i': 1, 'j': 1}

    # Test case 4
    assert task_func(10, 456) == {'a': 2, 'b': 2, 'c': 2, 'd': 2, 'e': 2, 'f': 1, 'g': 1, 'h': 1, 'i': 1, 'j': 1}