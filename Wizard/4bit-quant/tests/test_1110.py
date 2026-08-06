python
import os
import pytest
from src_1110 import task_func

def test_task_func():
    # Test case 1: Valid file path
    file_path = 'File.txt'
    assert os.path.isfile(file_path)
    tokens = task_func(file_path)
    assert isinstance(tokens, list)
    assert len(tokens) > 0

    # Test case 2: Invalid file path
    file_path = 'Invalid.txt'
    assert not os.path.isfile(file_path)
    with pytest.raises(FileNotFoundError):
        task_func(file_path)