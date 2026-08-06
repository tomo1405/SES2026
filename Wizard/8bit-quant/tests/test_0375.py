python
import pytest
from src_0375 import task_func

def test_task_func():
    # Test case 1: Directory does not exist
    with pytest.raises(FileNotFoundError):
        task_func('nonexistent_directory')

    # Test case 2: Directory exists but no xlsx files
    with pytest.raises(FileNotFoundError):
        task_func('empty_directory')

    # Test case 3: Directory exists and contains xlsx files
    processed_files = task_func('test_directory')
    assert processed_files == 2

    # Test case 4: Directory exists and contains xlsx files with no strings
    processed_files = task_func('test_directory_no_strings')
    assert processed_files == 0

    # Test case 5: Directory exists and contains xlsx files with strings
    processed_files = task_func('test_directory_with_strings')
    assert processed_files == 2