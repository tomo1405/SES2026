import pytest
from src_0972 import task_func
from pathlib import Path
from datetime import datetime, timezone
import os

def test_task_func_valid_directory(tmpdir):
    # Create a temporary directory and some files
    dir_path = tmpdir.mkdir("test_dir")
    file1 = dir_path.join("file1.txt")
    file2 = dir_path.join("file2.txt")
    file1.write("content1")
    file2.write("content2")

    # Call the function
    result = task_func(str(dir_path))

    # Check the result
    assert len(result) == 2
    for file_name, size, creation_time, modification_time in result:
        assert file_name in ["file1.txt", "file2.txt"]
        assert size in [len("content1"), len("content2")]
        assert isinstance(creation_time, str)
        assert isinstance(modification_time, str)

def test_task_func_invalid_directory():
    with pytest.raises(ValueError) as excinfo:
        task_func("/nonexistent_directory")
    assert str(excinfo.value) == "The path /nonexistent_directory is not a valid directory."

def test_task_func_empty_directory(tmpdir):
    # Create an empty temporary directory
    dir_path = tmpdir.mkdir("empty_dir")

    # Call the function
    result = task_func(str(dir_path))

    # Check the result
    assert result == []

def test_task_func_with_subdirectories(tmpdir):
    # Create a temporary directory and some files including subdirectories
    dir_path = tmpdir.mkdir("test_dir")
    sub_dir = dir_path.mkdir("sub_dir")
    file1 = dir_path.join("file1.txt")
    file2 = sub_dir.join("file2.txt")
    file1.write("content1")
    file2.write("content2")

    # Call the function
    result = task_func(str(dir_path))

    # Check the result
    assert len(result) == 1
    for file_name, size, creation_time, modification_time in result:
        assert file_name == "file1.txt"
        assert size == len("content1")
        assert isinstance(creation_time, str)
        assert isinstance(modification_time, str)