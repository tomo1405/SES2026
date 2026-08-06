python
import os
import logging
import pytest

from src_0307 import task_func

def test_task_func():
    # Test with valid directory
    directory = 'tests/test_files'
    removed_files, removed_file_names = task_func(directory)
    assert removed_files == 1
    assert removed_file_names == ['jquery-3.5.1.min.js']

    # Test with invalid directory
    with pytest.raises(FileNotFoundError):
        task_func('invalid_directory')

    # Test with directory that does not exist
    with pytest.raises(FileNotFoundError):
        task_func('nonexistent_directory')