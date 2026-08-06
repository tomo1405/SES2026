import pytest
from src_0336 import task_func

def test_task_func():
    assert task_func(100) == {'a': 20, 'b': 19, 'c': 18, 'd': 17, 'e': 16}
    assert task_func(5) == {'e': 4, 'd': 3, 'c': 2, 'b': 1, 'a': 0}
    assert task_func(1) == {'e': 1, 'd': 0, 'c': 0, 'b': 0, 'a': 0}
    assert task_func(1000) == {'a': 200, 'b': 199, 'c': 198, 'd': 197, 'e': 196}