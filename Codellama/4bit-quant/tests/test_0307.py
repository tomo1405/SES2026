import pytest
from src_0307 import task_func

def test_task_func():
    # Test case 1: directory exists
    directory = 'path/to/directory'
    expected_removed_files = 2
    expected_removed_file_names = ['jquery.js', 'jquery.min.js']
    removed_files, removed_file_names = task_func(directory)
    assert removed_files == expected_removed_files
    assert removed_file_names == expected_removed_file_names

    # Test case 2: directory does not exist
    directory = 'path/to/non-existent/directory'
    with pytest.raises(FileNotFoundError):
        task_func(directory)

    # Test case 3: directory exists but no jQuery files
    directory = 'path/to/directory'
    expected_removed_files = 0
    expected_removed_file_names = []
    removed_files, removed_file_names = task_func(directory)
    assert removed_files == expected_removed_files
    assert removed_file_names == expected_removed_file_names