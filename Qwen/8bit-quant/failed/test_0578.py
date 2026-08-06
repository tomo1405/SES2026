import pytest
from src_0578 import task_func
import os
import pathlib
from hashlib import md5
import unicodedata

def test_task_func(tmp_path):
    # Create some test files
    file1 = tmp_path / "test_file1.txt"
    file2 = tmp_path / "test_file2.txt"
    file3 = tmp_path / "test_file3.txt"

    file1.write_text("Hello, world!")
    file2.write_text("This is a test.")
    file3.write_text("Another test file.")

    # Expected results
    expected_files_info = {
        'test_file1.txt': {'Size': 13, 'MD5 Hash': '65a8e27d8879283831b664bd8b7f0ad4'},
        'test_file2.txt': {'Size': 15, 'MD5 Hash': 'c9b244a3b2d1a1a3a1a1a1a1a1a1a1a1'},
        'test_file3.txt': {'Size': 17, 'MD5 Hash': 'd41d8cd98f00b204e9800998ecf8427e'}
    }

    # Calculate the actual MD5 hashes for comparison
    for file in [file1, file2, file3]:
        with open(file, 'rb') as f:
            content = f.read()
            expected_files_info[file.name]['MD5 Hash'] = md5(content).hexdigest()

    # Run the function
    result = task_func(tmp_path)

    # Assert the results
    assert result == expected_files_info

def test_task_func_empty_directory(tmp_path):
    # No files created in this directory
    expected_files_info = {}

    # Run the function
    result = task_func(tmp_path)

    # Assert the results
    assert result == expected_files_info

def test_task_func_nonexistent_directory():
    # Test with a non-existent directory
    with pytest.raises(FileNotFoundError):
        task_func("nonexistent_directory")