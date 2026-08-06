python
import collections
import string
import random
import pytest

def task_func(length, seed=0):
    random.seed(seed)
    random_string = ''.join(random.choice(string.ascii_letters) for _ in range(length))

    char_freq = collections.Counter(random_string)

    return dict(char_freq)

def test_task_func():
    # Test case 1
    assert task_func(10, 0) == {'a': 2, 'b': 2, 'c': 1, 'd': 1, 'e': 1, 'f': 1, 'g': 1, 'h': 1, 'i': 1, 'j': 1}

    # Test case 2
    assert task_func(10, 1) == {'a': 2, 'b': 2, 'c': 1, 'd': 1, 'e': 1, 'f': 1, 'g': 1, 'h': 1, 'i': 1, 'j': 1}

    # Test case 3
    assert task_func(10, 2) == {'a': 2, 'b': 2, 'c': 1, 'd': 1, 'e': 1, 'f': 1, 'g': 1, 'h': 1, 'i': 1, 'j': 1}

    # Test case 4
    assert task_func(10, 3) == {'a': 2, 'b': 2, 'c': 1, 'd': 1, 'e': 1, 'f': 1, 'g': 1, 'h': 1, 'i': 1, 'j': 1}

    # Test case 5
    assert task_func(10, 4) == {'a': 2, 'b': 2, 'c': 1, 'd': 1, 'e': 1, 'f': 1, 'g': 1, 'h': 1, 'i': 1, 'j': 1}

    # Test case 6
    assert task_func(10, 5) == {'a': 2, 'b': 2, 'c': 1, 'd': 1, 'e': 1, 'f': 1, 'g': 1, 'h': 1, 'i': 1, 'j': 1}

    # Test case 7
    assert task_func(10, 6) == {'a': 2, 'b': 2, 'c': 1, 'd': 1, 'e': 1, 'f': 1, 'g': 1, 'h': 1, 'i': 1, 'j': 1}

    # Test case 8
    assert task_func(10, 7) == {'a': 2, 'b': 2, 'c': 1, 'd': 1, 'e': 1, 'f': 1, 'g': 1, 'h': 1, 'i': 1, 'j': 1}

    # Test case 9
    assert task_func(10, 8) == {'a': 2, 'b': 2, 'c': 1, 'd': 1, 'e': 1, 'f': 1, 'g': 1, 'h': 1, 'i': 1, 'j': 1}

    # Test case 10
    assert task_func(10, 9) == {'a': 2, 'b': 2, 'c': 1, 'd': 1, 'e': 1, 'f': 1, 'g': 1, 'h': 1, 'i': 1, 'j': 1}