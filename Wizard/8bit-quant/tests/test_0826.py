python
import numpy as np
import string
from itertools import product
import pytest

def task_func(length, seed=None, alphabets=list(string.ascii_lowercase)):
    np.random.seed(seed)
    all_combinations = [''.join(p) for p in product(alphabets, repeat=length)]
    return np.random.choice(all_combinations, size=10).tolist()

def test_task_func():
    # Test case 1: length=3, seed=None, alphabets=list(string.ascii_lowercase)
    assert task_func(3) == ['aaa', 'aab', 'aac', 'aba', 'abb', 'abc', 'aca', 'acb', 'acc']

    # Test case 2: length=4, seed=123, alphabets=['a', 'b', 'c']
    assert task_func(4, seed=123, alphabets=['a', 'b', 'c']) == ['aaa', 'aab', 'aac', 'aba', 'abb', 'abc', 'aca', 'acb', 'acc']

    # Test case 3: length=5, seed=456, alphabets=['d', 'e', 'f']
    assert task_func(5, seed=456, alphabets=['d', 'e', 'f']) == ['aaaaa', 'aaaba', 'aaaca', 'aaada', 'aabaa', 'aabab', 'aabba', 'aabca', 'aabda']

    # Test case 4: length=6, seed=789, alphabets=['g', 'h', 'i']
    assert task_func(6, seed=789, alphabets=['g', 'h', 'i']) == ['aaaaaa', 'aaaaba', 'aaaaca', 'aaaada', 'aaabaa', 'aaabab', 'aaabba', 'aaabca', 'aaabda']

    # Test case 5: length=7, seed=101112, alphabets=['j', 'k', 'l']
    assert task_func(7, seed=101112, alphabets=['j', 'k', 'l']) == ['aaaaaaaa', 'aaaaaba', 'aaaaaca', 'aaaaada', 'aaabaaa', 'aaababa', 'aaababb', 'aaabaca', 'aaabada']

    # Test case 6: length=8, seed=13141516, alphabets=['m', 'n', 'o']
    assert task_func(8, seed=13141516, alphabets=['m', 'n', 'o']) == ['aaaaaaaaa', 'aaaaaaab', 'aaaaaaac', 'aaaaaaad', 'aaaaabaa', 'aaaaabab', 'aaaaabba', 'aaaaabca', 'aaaaabda']

    # Test case 7: length=9, seed=16171819, alphabets=['p', 'q', 'r', 's']
    assert task_func(9, seed=16171819, alphabets=['p', 'q', 'r', 's']) == ['aaaaaaaaaa', 'aaaaaaaab', 'aaaaaaaac', 'aaaaaaaad', 'aaaaaaaba', 'aaaaaaabb', 'aaaaaaabc', 'aaaaaaabd', 'aaaaaabaa']

    # Test case 8: length=10, seed=19202122, alphabets=['t', 'u', 'v', 'w', 'x']
    assert task_func(10, seed=19202122, alphabets=['t', 'u', 'v', 'w', 'x']) == ['aaaaaaaaaaa', 'aaaaaaaaab', 'aaaaaaaaac', 'aaaaaaaaad', 'aaaaaaaaba', 'aaaaaaaabb', 'aaaaaaaabc', 'aaaaaaaabd', 'aaaaaaaaca', 'aaaaaaaacb']

    # Test case 9: length=11, seed=22232425, alphabets=['y', 'z']
    assert task_func(11, seed=22232425, alphabets=['y', 'z']) == ['aaaaaaaaaaaa', 'aaaaaaaaaaab', 'aaaaaaaaaaac', 'aaaaaaaaaaad', 'aaaaaaaaabaa', 'aaaaaaaaabab', 'aaaaaaaaabba', 'aaaaaaaaabca', 'aaaaaaaaabda', 'aaaaaaaaacaa']

    # Test case 10: length=12, seed=25262728, alphabets=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    assert task_func(12, seed=25262728, alphabets=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']) == ['aaaaaaaaaaaaaa', 'aaaaaaaaaaaaab', 'aaaaaaaaaaaaac', 'aaaaaaaaaaaaad', 'aaaaaaaaaaaaba', 'aaaaaaaaaaaabb', 'aaaaaaaaaaaabc', 'aaaaaaaaaaaabd', 'aaaaaaaaaaabaa', 'aaaaaaaaaaabab']