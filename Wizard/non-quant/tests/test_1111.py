python
import pytest
from src_1111 import task_func

def test_task_func():
    word_dict = {'apple': 1, 'banana': 2, 'cherry': 3, 'date': 4, 'elderberry': 5}
    expected_result = {'e': 5, 'r': 4, 'd': 4, 'a': 3, 'b': 2, 'c': 2, 'l': 1, 'n': 2, 'p': 1}
    assert task_func(word_dict) == expected_result