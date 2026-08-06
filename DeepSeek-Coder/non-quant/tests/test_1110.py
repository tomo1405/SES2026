import pytest
from src_1110 import task_func
import os

def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        task_func('nonexistent_file.txt')

def test_file_exists():
    result = task_func('test_file.txt')
    assert isinstance(result, list), "The result should be a list"
    assert len(result) > 0, "The result should not be empty"