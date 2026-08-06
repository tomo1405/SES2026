import pytest
from src_0862 import task_func

def test_task_func():
    # Test with empty list
    assert task_func([]) == []

    # Test with a single list
    assert task_func([['apple', 'banana', 'cherry']]) == [Counter({'apple': 1, 'banana': 1, 'cherry': 1})]

    # Test with multiple lists
    assert task_func([['apple', 'banana', 'cherry'], ['date', 'elderberry']]) == [Counter({'apple': 1, 'banana': 1, 'cherry': 1}), Counter({'date': 1, 'elderberry': 1})]

    # Test with different lengths
    assert task_func([['apple', 'banana', 'cherry'], ['date', 'elderberry'], ['apple', 'banana', 'cherry', 'date']]) == [Counter({'apple': 1, 'banana': 1, 'cherry': 1}), Counter({'date': 1, 'elderberry': 1}), Counter({'apple': 2, 'banana': 1, 'cherry': 1, 'date': 1})]

    # Test with different items
    assert task_func([['apple', 'banana', 'cherry'], ['date', 'elderberry'], ['apple', 'banana', 'cherry', 'date']]) == [Counter({'apple': 1, 'banana': 1, 'cherry': 1}), Counter({'date': 1, 'elderberry': 1}), Counter({'apple': 2, 'banana': 1, 'cherry': 1, 'date': 1})]

    # Test with different lengths and items
    assert task_func([['apple', 'banana', 'cherry'], ['date', 'elderberry'], ['apple', 'banana', 'cherry', 'date']]) == [Counter({'apple': 1, 'banana': 1, 'cherry': 1}), Counter({'date': 1, 'elderberry': 1}), Counter({'apple': 2, 'banana': 1, 'cherry': 1, 'date': 1})]