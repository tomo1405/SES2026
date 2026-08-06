import pytest
from collections import Counter
import itertools
import random
# Constants
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
def task_func(list_of_lists, seed=0):
    random.seed(seed)
    flattened_list = list(itertools.chain(*list_of_lists))

    for list_item in list_of_lists:
        if list_item == []:
            flattened_list += random.sample(ALPHABET, 10)

    counter = Counter(flattened_list)
    
    return counter

def test_task_func():
    list_of_lists = [[1, 2, 3], [4, 5, 6], [], [7, 8, 9]]
    seed = 0
    expected_result = Counter({1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1, 'g': 1, 'h': 1, 'i': 1, 'j': 1, 'k': 1, 'l': 1, 'm': 1, 'n': 1, 'o': 1, 'p': 1, 'q': 1, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 1, 'w': 1, 'x': 1, 'y': 1, 'z': 1})
    actual_result = task_func(list_of_lists, seed)
    assert actual_result == expected_result

def test_task_func_with_seed_1():
    list_of_lists = [[1, 2, 3], [4, 5, 6], [], [7, 8, 9]]
    seed = 1
    expected_result = Counter({1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1, 'g': 1, 'h': 1, 'i': 1, 'j': 1, 'k': 1, 'l': 1, 'm': 1, 'n': 1, 'o': 1, 'p': 1, 'q': 1, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 1, 'w': 1, 'x': 1, 'y': 1, 'z': 1})
    actual_result = task_func(list_of_lists, seed)
    assert actual_result == expected_result

def test_task_func_with_empty_list():
    list_of_lists = [[]]
    seed = 0
    expected_result = Counter({'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1, 'g': 1, 'h': 1, 'i': 1, 'j': 1, 'k': 1, 'l': 1, 'm': 1, 'n': 1, 'o': 1, 'p': 1, 'q': 1, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 1, 'w': 1, 'x': 1, 'y': 1, 'z': 1})
    actual_result = task_func(list_of_lists, seed)
    assert actual_result == expected_result

def test_task_func_with_empty_list_and_seed_1():
    list_of_lists = [[]]
    seed = 1
    expected_result = Counter({'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1, 'g': 1, 'h': 1, 'i': 1, 'j': 1, 'k': 1, 'l': 1, 'm': 1, 'n': 1, 'o': 1, 'p': 1, 'q': 1, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 1, 'w': 1, 'x': 1, 'y': 1, 'z': 1})
    actual_result = task_func(list_of_lists, seed)
    assert actual_result == expected_result