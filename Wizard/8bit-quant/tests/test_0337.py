python
import pytest
from src_0337 import task_func

def test_task_func():
    pattern = 'test'
    directory = '.'
    extensions = ['*.txt', '*.py']
    expected_result = [Path('test.txt').resolve(), Path('test.py').resolve()]
    assert task_func(pattern, directory, extensions) == expected_result