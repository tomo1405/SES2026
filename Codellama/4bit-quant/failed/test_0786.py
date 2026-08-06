import pytest
from src_0786 import task_func

def test_task_func():
    # Test case 1: No files found matching the pattern
    pattern = '*.txt'
    file_list = []
    expected_output = "No files found matching the pattern."
    assert task_func(pattern) == expected_output

    # Test case 2: One file found matching the pattern
    pattern = '*.txt'
    file_list = ['file1.txt']
    expected_output = 'archive.tar.gz'
    assert task_func(pattern) == expected_output

    # Test case 3: Multiple files found matching the pattern
    pattern = '*.txt'
    file_list = ['file1.txt', 'file2.txt', 'file3.txt']
    expected_output = 'archive.tar.gz'
    assert task_func(pattern) == expected_output

    # Test case 4: No files found matching the pattern, but archive directory exists
    pattern = '*.txt'
    file_list = []
    expected_output = "No files found matching the pattern."
    assert task_func(pattern) == expected_output

    # Test case 5: One file found matching the pattern, but archive directory exists
    pattern = '*.txt'
    file_list = ['file1.txt']
    expected_output = 'archive.tar.gz'
    assert task_func(pattern) == expected_output

    # Test case 6: Multiple files found matching the pattern, but archive directory exists
    pattern = '*.txt'
    file_list = ['file1.txt', 'file2.txt', 'file3.txt']
    expected_output = 'archive.tar.gz'
    assert task_func(pattern) == expected_output

    # Test case 7: No files found matching the pattern, but archive directory does not exist
    pattern = '*.txt'
    file_list = []
    expected_output = "No files found matching the pattern."
    assert task_func(pattern) == expected_output

    # Test case 8: One file found matching the pattern, but archive directory does not exist
    pattern = '*.txt'
    file_list = ['file1.txt']
    expected_output = 'archive.tar.gz'
    assert task_func(pattern) == expected_output

    # Test case 9: Multiple files found matching the pattern, but archive directory does not exist
    pattern = '*.txt'
    file_list = ['file1.txt', 'file2.txt', 'file3.txt']
    expected_output = 'archive.tar.gz'
    assert task_func(pattern) == expected_output