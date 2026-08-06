import pytest
from src_1111 import task_func

def test_task_func():
    word_dict = {'hello': 1, 'world': 2, 'python': 3}
    expected_result = {'h': 1, 'w': 1, 'p': 1, 'y': 1, 'l': 2, 'o': 2, 'r': 2, 'd': 2}
    assert task_func(word_dict) == expected_result