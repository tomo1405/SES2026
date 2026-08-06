python
import shutil
import pathlib
import pytest

from src_0975 import task_func

def test_task_func():
    source_path = "tests/test_data/source_dir"
    destination_path = "tests/test_data/destination_dir"

    # Test with valid input
    result = task_func(source_path, destination_path)
    assert result == ("source_dir", ["file1.txt", "file2.txt", "file3.txt"])

    # Test with invalid input (source_path is not a directory)
    with pytest.raises(ValueError):
        task_func("tests/test_data/file1.txt", destination_path)

    # Test with invalid input (destination_path is not a directory)
    with pytest.raises(ValueError):
        task_func(source_path, "tests/test_data/file1.txt")

    # Test with invalid input (source_path does not exist)
    with pytest.raises(ValueError):
        task_func("tests/test_data/nonexistent_dir", destination_path)

    # Test with invalid input (destination_path does not exist)
    with pytest.raises(ValueError):
        task_func(source_path, "tests/test_data/nonexistent_dir")