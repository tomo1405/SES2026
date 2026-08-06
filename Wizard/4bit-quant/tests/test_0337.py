python
import pytest
from src_0337 import task_func

def test_task_func():
    pattern = 'test'
    directory = '.'
    extensions = ['*.txt', '*.md']
    expected_result = [Path('test.txt').resolve(), Path('test.md').resolve()]
    result = task_func(pattern, directory, extensions)
    assert result == expected_result