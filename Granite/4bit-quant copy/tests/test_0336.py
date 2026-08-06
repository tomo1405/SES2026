import pytest
from src_0336 import task_func

def test_task_func():
    assert task_func(100) == {'a': 16, 'b': 16, 'c': 16, 'd': 16, 'e': 16}
    assert task_func(5) == {'e': 5, 'd': 4, 'a': 3, 'b': 2, 'c': 1}
    assert task_func(1) == {'e': 1, 'd': 1, 'a': 1, 'b': 1, 'c': 1}
    assert task_func(10) == {'e': 5, 'd': 4, 'a': 3, 'b': 2, 'c': 1}