python
import pytest
from src_0862 import task_func

def test_task_func():
    # Test case 1
    list_of_lists = [
        ['apple', 'banana', 'cherry'],
        ['date', 'elderberry', 'apple', 'banana'],
        ['cherry', 'apple', 'banana', 'date', 'elderberry']
    ]
    expected_baskets = [
        {'apple': 1, 'banana': 1, 'cherry': 1},
        {'date': 1, 'elderberry': 1, 'apple': 1, 'banana': 1},
        {'cherry': 1, 'apple': 1, 'banana': 1, 'date': 1, 'elderberry': 1}
    ]
    assert task_func(list_of_lists) == expected_baskets

    # Test case 2
    list_of_lists = [
        ['apple', 'banana', 'cherry'],
        ['date', 'elderberry', 'apple', 'banana'],
        ['cherry', 'apple', 'banana', 'date', 'elderberry']
    ]
    expected_baskets = [
        {'apple': 1, 'banana': 1, 'cherry': 1},
        {'date': 1, 'elderberry': 1, 'apple': 1, 'banana': 1},
        {'cherry': 1, 'apple': 1, 'banana': 1, 'date': 1, 'elderberry': 1}
    ]
    assert task_func(list_of_lists) == expected_baskets

    # Test case 3
    list_of_lists = [
        ['apple', 'banana', 'cherry'],
        ['date', 'elderberry', 'apple', 'banana'],
        ['cherry', 'apple', 'banana', 'date', 'elderberry']
    ]
    expected_baskets = [
        {'apple': 1, 'banana': 1, 'cherry': 1},
        {'date': 1, 'elderberry': 1, 'apple': 1, 'banana': 1},
        {'cherry': 1, 'apple': 1, 'banana': 1, 'date': 1, 'elderberry': 1}
    ]
    assert task_func(list_of_lists) == expected_baskets