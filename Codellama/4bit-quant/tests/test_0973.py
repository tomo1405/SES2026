import pytest
from src_0973 import task_func

def test_task_func():
    # Test case 1: empty path
    assert task_func("") == []

    # Test case 2: path with invalid characters
    assert task_func("path/to/file.txt", delimiter=".") == []

    # Test case 3: path with valid characters
    assert task_func("path/to/file.txt", delimiter=".") == ["path", "to", "file.txt"]

    # Test case 4: path with multiple delimiters
    assert task_func("path/to/file.txt", delimiter=".") == ["path", "to", "file.txt"]

    # Test case 5: path with multiple delimiters and invalid characters
    assert task_func("path/to/file.txt", delimiter=".") == ["path", "to", "file.txt"]

    # Test case 6: path with multiple delimiters and invalid characters
    assert task_func("path/to/file.txt", delimiter=".") == ["path", "to", "file.txt"]

    # Test case 7: path with multiple delimiters and invalid characters
    assert task_func("path/to/file.txt", delimiter=".") == ["path", "to", "file.txt"]

    # Test case 8: path with multiple delimiters and invalid characters
    assert task_func("path/to/file.txt", delimiter=".") == ["path", "to", "file.txt"]

    # Test case 9: path with multiple delimiters and invalid characters
    assert task_func("path/to/file.txt", delimiter=".") == ["path", "to", "file.txt"]

    # Test case 10: path with multiple delimiters and invalid characters
    assert task_func("path/to/file.txt", delimiter=".") == ["path", "to", "file.txt"]