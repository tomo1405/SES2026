import pytest
from src_0782 import task_func
from datetime import datetime
import os

def test_task_func_valid_file(tmp_path):
    # Create a temporary file and write some data to it
    file_path = tmp_path / "test_file.txt"
    with open(file_path, "w") as f:
        f.write("Hello, world!")

    # Get the expected size and modification time
    expected_size = os.path.getsize(file_path)
    expected_mtime = datetime.fromtimestamp(os.path.getmtime(file_path)).strftime('%Y-%m-%d %H:%M:%S')

    # Call the function and check the result
    result = task_func(str(file_path))
    assert result == {'size': f"{expected_size} bytes", 'last_modified': expected_mtime}

def test_task_func_non_existent_file():
    # Define a non-existent file path
    file_path = "/path/to/non_existent_file.txt"

    # Check that the function raises an exception
    with pytest.raises(Exception) as exc_info:
        task_func(file_path)
    assert str(exc_info.value) == "Error: [Errno 2] No such file or directory: '/path/to/non_existent_file.txt'"

def test_task_func_directory(tmp_path):
    # Create a temporary directory
    dir_path = tmp_path / "test_dir"
    dir_path.mkdir()

    # Check that the function raises an exception for a directory
    with pytest.raises(Exception) as exc_info:
        task_func(str(dir_path))
    assert str(exc_info.value) == "Error: [Errno 21] Is a directory: '" + str(dir_path) + "'"