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
    n = 10
    seed = 123
    expected_result = {'a': ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
                       'b': ['b'],
                       'c': ['c'],
                       'd': ['d'],
                       'e': ['e'],
                       'f': ['f'],
                       'g': ['g'],
                       'h': ['h'],
                       'i': ['i'],
                       'j': ['j'],
                       'k': ['k'],
                       'l': ['l'],
                       'm': ['m'],
                       'n': ['n'],
                       'o': ['o'],
                       'p': ['p'],
                       'q': ['q'],
                       'r': ['r'],
                       's': ['s'],
                       't': ['t'],
                       'u': ['u'],
                       'v': ['v'],
                       'w': ['w'],
                       'x': ['x'],
                       'y': ['y'],
                       'z': ['z']}
    assert task_func(n, seed) == expected_result

    # Test case 2
    n = 100
    seed = 456
    expected_result = {'a': ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
                       'b': ['b'],
                       'c': ['c'],
                       'd': ['d'],
                       'e': ['e'],
                       'f': ['f'],
                       'g': ['g'],
                       'h': ['h'],
                       'i': ['i'],
                       'j': ['j'],
                       'k': ['k'],
                       'l': ['l'],
                       'm': ['m'],
                       'n': ['n'],
                       'o': ['o'],
                       'p': ['p'],
                       'q': ['q'],
                       'r': ['r'],
                       's': ['s'],
                       't': ['t'],
                       'u': ['u'],
                       'v': ['v'],
                       'w': ['w'],
                       'x': ['x'],
                       'y': ['y'],
                       'z': ['z']}
    assert task_func(n, seed) == expected_result

    # Test case 3
    n = 0
    seed = 789
    expected_result = {}
    assert task_func(n, seed) == expected_result

    # Test case 4
    n = 1
    seed = 101112
    expected_result = {'a': ['a']}
    assert task_func(n, seed) == expected_result

    # Test case 5
    n = 1000000
    seed = 131415
    expected_result = {'a': ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
                       'b': ['b'],
                       'c': ['c'],
                       'd': ['d'],
                       'e': ['e'],
                       'f': ['f'],
                       'g': ['g'],
                       'h': ['h'],
                       'i': ['i'],
                       'j': ['j'],
                       'k': ['k'],
                       'l': ['l'],
                       'm': ['m'],
                       'n': ['n'],
                       'o': ['o'],
                       'p': ['p'],
                       'q': ['q'],
                       'r': ['r'],
                       's': ['s'],
                       't': ['t'],
                       'u': ['u'],
                       'v': ['v'],
                       'w': ['w'],
                       'x': ['x'],
                       'y': ['y'],
                       'z': ['z']}
    assert task_func(n, seed) == expected_result