import pytest
from src_0326 import task_func
import os
from pathlib import Path

# Mocking utilities
from unittest.mock import patch, mock_open

@pytest.fixture
def mock_directory(tmpdir):
    # Create a temporary directory and some text files for testing
    dir_path = tmpdir.mkdir("test_dir")
    file1 = dir_path.join("file1.txt")
    file2 = dir_path.join("file2.txt")
    file1.write("hello world")
    file2.write("foo bar baz")
    return str(dir_path)

def test_task_func_no_files(mock_directory):
    # Test case where no .txt files exist in the directory
    empty_dir = mock_directory + "_empty"
    os.makedirs(empty_dir)
    result = task_func(empty_dir)
    assert result == {}

def test_task_func_single_file(mock_directory):
    # Test case with a single .txt file
    result = task_func(mock_directory)
    expected = {
        "file1.txt": ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
    }
    assert result == expected

def test_task_func_multiple_files(mock_directory):
    # Test case with multiple .txt files
    result = task_func(mock_directory)
    expected = {
        "file1.txt": ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd'],
        "file2.txt": ['f', 'o', 'o', ' ', 'b', 'a', 'r', ' ', 'b', 'a', 'z']
    }
    assert result == expected

@patch('glob.glob')
def test_task_func_nonexistent_directory(mock_glob):
    # Test case where the directory does not exist
    mock_glob.return_value = []
    result = task_func("/nonexistent/directory")
    assert result == {}

@patch('builtins.open', new_callable=mock_open, read_data="test data")
def test_task_func_custom_regex(mock_file, mock_directory):
    # Test case with a custom regex pattern
    regex_pattern = r'\b\w+\b'
    result = task_func(mock_directory, regex_pattern)
    expected = {
        "file1.txt": ['hello', 'world'],
        "file2.txt": ['foo', 'bar', 'baz']
    }
    assert result == expected