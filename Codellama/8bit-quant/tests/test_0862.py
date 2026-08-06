from typing import Counter

from src_0862 import task_func


def test_task_func():
    list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected_baskets = [
        Counter({'apple': 1, 'banana': 1, 'cherry': 1}),
        Counter({'date': 1, 'elderberry': 1, 'banana': 1}),
        Counter({'cherry': 1, 'elderberry': 1, 'apple': 1})
    ]
    assert task_func(list_of_lists) == expected_baskets