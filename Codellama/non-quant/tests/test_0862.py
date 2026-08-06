from typing import Counter

from src_0862 import task_func


def test_task_func():
    # Test case 1: Empty list
    list_of_lists = []
    expected_result = []
    assert task_func(list_of_lists) == expected_result

    # Test case 2: Single list
    list_of_lists = [['apple', 'banana', 'cherry']]
    expected_result = [Counter({'apple': 1, 'banana': 1, 'cherry': 1})]
    assert task_func(list_of_lists) == expected_result

    # Test case 3: Multiple lists
    list_of_lists = [['apple', 'banana', 'cherry'], ['date', 'elderberry']]
    expected_result = [Counter({'apple': 1, 'banana': 1, 'cherry': 1}), Counter({'date': 1, 'elderberry': 1})]
    assert task_func(list_of_lists) == expected_result

    # Test case 4: Lists with different lengths
    list_of_lists = [['apple', 'banana', 'cherry'], ['date', 'elderberry', 'apple']]
    expected_result = [Counter({'apple': 1, 'banana': 1, 'cherry': 1}), Counter({'date': 1, 'elderberry': 1, 'apple': 1})]
    assert task_func(list_of_lists) == expected_result

    # Test case 5: Lists with duplicates
    list_of_lists = [['apple', 'banana', 'cherry'], ['date', 'elderberry', 'apple', 'apple']]
    expected_result = [Counter({'apple': 1, 'banana': 1, 'cherry': 1}), Counter({'date': 1, 'elderberry': 1, 'apple': 2})]
    assert task_func(list_of_lists) == expected_result