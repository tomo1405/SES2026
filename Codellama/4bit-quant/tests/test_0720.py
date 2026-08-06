import pytest
from src_0720 import task_func

def test_task_func():
    directory = 'path/to/directory'
    word = 'hello'
    expected_count = 5
    actual_count = task_func(directory, word)
    assert actual_count == expected_count