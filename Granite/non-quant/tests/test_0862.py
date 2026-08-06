import pytest
from collections import Counter
from random import choice, seed
from src_0862 import task_func
POSSIBLE_ITEMS = ['apple', 'banana', 'cherry', 'date', 'elderberry']

def test_task_func():
    list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    seed(42)  # Set the seed for reproducibility
    expected_output = [
        Counter({'banana': 2, 'apple': 1, 'cherry': 1, 'date': 1, 'elderberry': 1}),
        Counter({'banana': 2, 'apple': 1, 'cherry': 1, 'date': 1, 'elderberry': 1}),
        Counter({'banana': 2, 'apple': 1, 'cherry': 1, 'date': 1, 'elderberry': 1})
    ]
    actual_output = task_func(list_of_lists)
    assert actual_output == expected_output

def test_task_func_with_empty_list():
    list_of_lists = [[], [], []]
    seed(42)  # Set the seed for reproducibility
    expected_output = [
        Counter(),
        Counter(),
        Counter()
    ]
    actual_output = task_func(list_of_lists)
    assert actual_output == expected_output

def test_task_func_with_single_item_list():
    list_of_lists = [['apple'], ['banana'], ['cherry']]
    seed(42)  # Set the seed for reproducibility
    expected_output = [
        Counter({'apple': 1}),
        Counter({'banana': 1}),
        Counter({'cherry': 1})
    ]
    actual_output = task_func(list_of_lists)
    assert actual_output == expected_output