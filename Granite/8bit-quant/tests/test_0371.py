from unittest.mock import patch

import pytest
from src_0371 import task_func


def test_task_func():
    directory_path = "/path/to/directory"
    expected_output = ["/path/to/directory/file1.json", "/path/to/directory/file2.json"]
    
    # Mock the os.path.exists function to return True
    mock_exists = lambda path: True
    with patch("os.path.exists", mock_exists):
        processed_files = task_func(directory_path)
    
    assert processed_files == expected_output

def test_task_func_file_not_found():
    directory_path = "/path/to/nonexistent_directory"
    expected_error_message = "Directory /path/to/nonexistent_directory not found."
    
    # Mock the os.path.exists function to return False
    mock_exists = lambda path: False
    with patch("os.path.exists", mock_exists):
        with pytest.raises(FileNotFoundError) as exc_info:
            task_func(directory_path)
    
    assert str(exc_info.value) == expected_error_message