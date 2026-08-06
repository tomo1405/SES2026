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
    assert task_func(5, seed=456, alphabets=['d', 'e', 'f']) == ['dddde', 'dddee', 'dddef', 'ddeed', 'ddefe', 'ddefd', 'deeef', 'deeed', 'deeef']

    # Test case 4: length=6, seed=789, alphabets=['g', 'h', 'i']
    assert task_func(6, seed=789, alphabets=['g', 'h', 'i']) == ['gggggg', 'gggggh', 'gggggi', 'gggghh', 'gggghi', 'ggghhh', 'ggghhi', 'gggiih', 'gggiii']