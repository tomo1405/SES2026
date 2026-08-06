python
import pytest
from src_1111 import task_func

def test_task_func():
    word_dict = {'apple': 1, 'banana': 2, 'cherry': 3}
    expected_result = {'e': 3, 'a': 2, 'p': 1, 'b': 1, 'n': 2, 'r': 1, 'y': 1}
    assert task_func(word_dict) == expected_result