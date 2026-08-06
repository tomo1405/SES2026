python
import pytest
from src_1111 import task_func

def test_task_func():
    word_dict = {'apple': 2, 'banana': 1, 'cherry': 3}
    expected_result = {'a': 3, 'b': 1, 'c': 3, 'e': 1, 'h': 1, 'n': 2, 'p': 1}
    assert task_func(word_dict) == expected_result