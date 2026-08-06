import pytest
from src_0782 import task_func
import os
from datetime import datetime

def test_task_func_valid_file(tmp_path):
    # Create a temporary file with some content
    test_file = tmp_path / "testfile.txt"
    test_file.write_text("Hello, World!")

    # Get the expected size and last modified time
    expected_size = test_file.stat().st_size
    expected_mtime = datetime.fromtimestamp(test_file.stat().st_mtime).strftime('%Y-%m-%d %H:%M:%S')

    # Call the function
    result = task_func(str(test_file))

    # Assert the results
    assert result['size'] == f"{expected_size} bytes"
    assert result['last_modified'] == expected_mtime

def test_task_func_non_existent_file():
    # Define a non-existent file path
    non_existent_file = "/path/to/non/existent/file"

    # Expect an exception to be raised
    with pytest.raises(Exception) as exc_info:
        task_func(non_existent_file)

    # Assert the exception message
    assert str(exc_info.value) == "Error: [Errno 2] No such file or directory: '/path/to/non/existent/file'"

def test_task_func_permission_denied(tmp_path):
    # Create a temporary directory and a file within it
    test_dir = tmp_path / "restricted_dir"
    test_dir.mkdir()
    test_file = test_dir / "testfile.txt"
    test_file.write_text("Hello, World!")

    # Change permissions to read-only
    os.chmod(test_dir, 0o444)

    # Expect an exception to be raised
    with pytest.raises(Exception) as exc_info:
        task_func(str(test_file))

    # Assert the exception message (the exact message may vary based on the OS)
    assert "Permission denied" in str(exc_info.value)

    # Reset permissions for cleanup
    os.chmod(test_dir, 0o777)