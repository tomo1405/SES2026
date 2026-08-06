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
    assert task_func(10) == {'a': 2, 'b': 2, 'c': 1, 'd': 1, 'e': 1, 'f': 1, 'g': 1, 'h': 1, 'i': 1, 'j': 1}

    # Test case 2: n=10, seed=1234
    assert task_func(10, seed=1234) == {'a': 2, 'b': 2, 'c': 1, 'd': 1, 'e': 1, 'f': 1, 'g': 1, 'h': 1, 'i': 1, 'j': 1}

    # Test case 3: n=0, seed=None
    assert task_func(0) == {}

    # Test case 4: n=0, seed=1234
    assert task_func(0, seed=1234) == {}

    # Test case 5: n=1, seed=None
    assert task_func(1) == {'a': 1}

    # Test case 6: n=1, seed=1234
    assert task_func(1, seed=1234) == {'a': 1}

    # Test case 7: n=1000, seed=None
    assert task_func(1000) == {'a': 249, 'b': 248, 'c': 247, 'd': 246, 'e': 245, 'f': 244, 'g': 243, 'h': 242, 'i': 241, 'j': 240}

    # Test case 8: n=1000, seed=1234
    assert task_func(1000, seed=1234) == {'a': 249, 'b': 248, 'c': 247, 'd': 246, 'e': 245, 'f': 244, 'g': 243, 'h': 242, 'i': 241, 'j': 240}