python
import pytest
from src_0326 import task_func

def test_task_func():
    # Test case 1
    directory_path = 'test_dir'
    regex_pattern = r'\\(.+?\\)|\\w'
    expected_result = {'file1.txt': ['hello', 'world'], 'file2.txt': ['foo', 'bar']}
    result = task_func(directory_path, regex_pattern)
    assert result == expected_result

    # Test case 2
    directory_path = 'test_dir'
    regex_pattern = r'\\b\\w+\\b'
    expected_result = {'file1.txt': ['hello', 'world'], 'file2.txt': ['foo', 'bar']}
    result = task_func(directory_path, regex_pattern)
    assert result == expected_result

    # Test case 3
    directory_path = 'test_dir'
    regex_pattern = r'\\d+'
    expected_result = {'file1.txt': [], 'file2.txt': []}
    result = task_func(directory_path, regex_pattern)
    assert result == expected_result