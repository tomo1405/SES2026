import pytest
from src_0578 import task_func
import os
import pathlib
from hashlib import md5
import unicodedata

# Mocking utilities
from unittest.mock import patch, mock_open

@pytest.fixture
def mock_directory(tmp_path):
    # Create a temporary directory with some test files
    dir_path = tmp_path / "test_dir"
    dir_path.mkdir()

    # Create test files
    file1 = dir_path / "file1.txt"
    file2 = dir_path / "file2.txt"
    file3 = dir_path / "file3.txt"

    file1.write_text("Hello, World!")
    file2.write_text("Python Testing")
    file3.write_text("Mocking is fun!")

    return str(dir_path)

def test_task_func(mock_directory):
    # Expected results
    expected_files_info = {
        'file1.txt': {'Size': 13, 'MD5 Hash': '65a8e27d8879283831b664bd8b7f0ad4'},
        'file2.txt': {'Size': 14, 'MD5 Hash': '3f53bf48d8c2d6b1e1f1033505d3c808'},
        'file3.txt': {'Size': 16, 'MD5 Hash': 'd3b07384d113edec49eaa6238ad5ff00'}
    }

    # Call the function with the mock directory
    result = task_func(mock_directory)

    # Assert that the result matches the expected output
    assert result == expected_files_info

@patch('pathlib.Path.iterdir')
def test_task_func_no_files(mock_iterdir, tmp_path):
    # Mock iterdir to return no files
    mock_iterdir.return_value = []

    # Call the function with an empty directory
    result = task_func(str(tmp_path))

    # Assert that the result is an empty dictionary
    assert result == {}

@patch('os.path.getsize', side_effect=[10, 20])
@patch('builtins.open', new_callable=mock_open, read_data=b'data')
def test_task_func_with_special_chars(mock_open, mock_getsize, tmp_path):
    # Create a temporary directory with a file containing special characters
    dir_path = tmp_path / "special_char_dir"
    dir_path.mkdir()

    file = dir_path / "file_with_special_chars.txt"
    file.write_text("Spécial Chars")

    # Expected results
    expected_files_info = {
        'file_with_special_chars.txt': {'Size': 20, 'MD5 Hash': '8d969eef6ecad3c29a3a629280e686cf'}
    }

    # Call the function with the mock directory
    result = task_func(str(dir_path))

    # Assert that the result matches the expected output
    assert result == expected_files_info