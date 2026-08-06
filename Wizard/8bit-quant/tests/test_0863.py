python
import random
import string
from collections import defaultdict
import pytest

def task_func(n, seed=None):
    LETTERS = string.ascii_lowercase
    random.seed(seed)
    letter_dict = defaultdict(list)
    for _ in range(n):
        letter = random.choice(LETTERS)
        letter_dict[letter].append(letter)
    return letter_dict

def test_task_func():
    # Test case 1
    assert task_func(10, 123) == {'a': ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'], 'b': ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'], 'c': ['c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c'], 'd': ['d', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd'], 'e': ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'], 'f': ['f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f'], 'g': ['g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g'], 'h': ['h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h'], 'i': ['i', 'i', 'i', 'i', 'i', 'i', 'i', 'i', 'i', 'i'], 'j': ['j', 'j', 'j', 'j', 'j', 'j', 'j', 'j', 'j', 'j']}

    # Test case 2
    assert task_func(5, 456) == {'a': ['a', 'a', 'a', 'a', 'a'], 'b': ['b', 'b', 'b', 'b', 'b'], 'c': ['c', 'c', 'c', 'c', 'c'], 'd': ['d', 'd', 'd', 'd', 'd'], 'e': ['e', 'e', 'e', 'e', 'e']}

    # Test case 3
    assert task_func(0, 789) == {}

    # Test case 4
    assert task_func(1, 101112) == {'a': ['a']}

    # Test case 5
    assert task_func(10, None) != {}