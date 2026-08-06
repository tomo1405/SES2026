import pytest
from src_0634 import task_func

def test_task_func():
    assert task_func("This is a test.") == {'a': 1, 'is': 1, 'test.': 1, 'this': 1}
    assert task_func("This is another test.") == {'a': 1, 'another': 1, 'is': 1, 'test.': 1, 'this': 1}
    assert task_func("This is a test with some words.") == {'a': 1, 'is': 1, 'some': 1, 'test': 1, 'words.': 1, 'with': 1, 'this': 1}