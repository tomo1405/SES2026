from datetime import datetime

import pytest
from src_1107 import task_func


def test_task_func_existing_file(tmp_path):
    # Create a temporary file
    temp_file = tmp_path / "test_file.txt"
    temp_file.write_text("Sample content")

    # Get the creation time of the file and format it
    expected_time = datetime.fromtimestamp(temp_file.stat().st_ctime).strftime('%Y-%m-%d %H:%M:%S')

    # Call the function and check if the output matches the expected time
    assert task_func(str(temp_file)) == expected_time

def test_task_func_non_existing_file():
    with pytest.raises(FileNotFoundError) as excinfo:
        task_func("/non/existing/path")
    assert str(excinfo.value) == "No such file or directory: '/non/existing/path'"

def test_task_func_directory(tmp_path):
    # Create a temporary directory
    temp_dir = tmp_path / "test_dir"
    temp_dir.mkdir()

    # Get the creation time of the directory and format it
    expected_time = datetime.fromtimestamp(temp_dir.stat().st_ctime).strftime('%Y-%m-%d %H:%M:%S')

    # Call the function and check if the output matches the expected time
    assert task_func(str(temp_dir)) == expected_time