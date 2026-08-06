import pytest
from src_0306 import task_func

def test_task_func():
    # Test case 1: empty list
    list_of_lists = []
    seed = 0
    expected_result = Counter()
    assert task_func(list_of_lists, seed) == expected_result

    # Test case 2: single list with no duplicates
    list_of_lists = [['a', 'b', 'c']]
    seed = 0
    expected_result = Counter({'a': 1, 'b': 1, 'c': 1})
    assert task_func(list_of_lists, seed) == expected_result

    # Test case 3: multiple lists with duplicates
    list_of_lists = [['a', 'b', 'c'], ['a', 'b', 'c']]
    seed = 0
    expected_result = Counter({'a': 2, 'b': 2, 'c': 2})
    assert task_func(list_of_lists, seed) == expected_result

    # Test case 4: empty list with random sample
    list_of_lists = []
    seed = 1
    expected_result = Counter()
    assert task_func(list_of_lists, seed) == expected_result

    # Test case 5: single list with random sample
    list_of_lists = [[]]
    seed = 1
    expected_result = Counter()
    assert task_func(list_of_lists, seed) == expected_result

    # Test case 6: multiple lists with random sample
    list_of_lists = [['a', 'b', 'c'], ['a', 'b', 'c']]
    seed = 1
    expected_result = Counter()
    assert task_func(list_of_lists, seed) == expected_result