import pytest
from src_0505 import task_func

def test_task_func():
    file_path = 'path/to/test/file'
    expected_signature = 'expected_signature'

    actual_signature = task_func(file_path)

    assert actual_signature == expected_signature