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
    # Test case 1: n=10, seed=None
    assert task_func(10) == Counter({'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1, 'g': 1, 'h': 1, 'i': 1, 'j': 1})

    # Test case 2: n=5, seed=123
    random.seed(123)
    assert task_func(5, seed=123) == Counter({'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1})

    # Test case 3: n=10, seed=456
    random.seed(456)
    assert task_func(10, seed=456) == Counter({'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1, 'g': 1, 'h': 1, 'i': 1, 'j': 1})