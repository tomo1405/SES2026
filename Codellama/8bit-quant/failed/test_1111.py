import pytest
from src_1111 import task_func

def test_task_func():
    word_dict = {'apple': 2, 'banana': 3, 'orange': 1}
    expected_result = {'a': 3, 'b': 2, 'o': 1}
    assert task_func(word_dict) == expected_result