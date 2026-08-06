python
import pytest
from src_1107 import task_func

def test_task_func():
    # Test case 1: Valid file path
    file_path = 'test.txt'
    expected_output = '2022-01-01 00:00:00'
    assert task_func(file_path) == expected_output
    
    # Test case 2: Invalid file path
    file_path = 'invalid.txt'
    with pytest.raises(FileNotFoundError):
        task_func(file_path)