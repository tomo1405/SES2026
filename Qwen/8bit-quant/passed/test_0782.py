import pytest
from src_0782 import task_func
import os
from datetime import datetime

def test_task_func_valid_file(tmp_path):
    # Create a temporary file
    test_file = tmp_path / "testfile.txt"
    test_file.write_text("Hello, world!")

    # Get the expected size and last modified time
    expected_size = test_file.stat().st_size
    expected_mtime = datetime.fromtimestamp(test_file.stat().st_mtime).strftime('%Y-%m-%d %H:%M:%S')

    # Call the function
    result = task_func(str(test_file))

    # Assert the results
    assert result['size'] == f"{expected_size} bytes"
    assert result['last_modified'] == expected_mtime

def test_task_func_nonexistent_file():
    # Use a non-existent file path
    filepath = "nonexistent_file.txt"

    # Expect an exception to be raised
    with pytest.raises(Exception) as excinfo:
        task_func(filepath)

    # Check the exception message
    assert "No such file or directory" in str(excinfo.value)