import re
from collections import Counter
from string import ascii_lowercase
from src_0776 import task_func

def test_task_func():
    assert task_func("abc-def") == {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 0}
    assert task_func("abc-xyz") == {'a': 1, 'b': 1, 'c': 1, 'x': 1, 'y': 1, 'z': 1}
    assert task_func("123-abc") == {'a': 1, 'b': 1, 'c': 1, '1': 0, '2': 0, '3': 0}
    assert task_func("abc") == {'a': 1, 'b': 1, 'c': 1}
    assert task_func("123") == {'1': 0, '2': 0, '3': 0}
    assert task_func("abc123") == {'a': 1, 'b': 1, 'c': 1, '1': 0, '2': 0, '3': 0}
    assert task_func("abc-def-ghi") == {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 0, 'g': 0, 'h': 0, 'i': 0}
    assert task_func("abc-def-ghi-jkl") == {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0}