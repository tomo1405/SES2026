python
import pathlib
import shutil
import pytest

from src_0975 import task_func

def test_task_func():
    source_path = pathlib.Path("tests/test_data/source_dir")
    destination_path = pathlib.Path("tests/test_data/destination_dir")

    # Test with valid input
    result = task_func(str(source_path), str(destination_path))
    assert result == ("source_dir", ["file1.txt", "file2.txt", "file3.txt"])

    # Test with invalid input (source_path is not a directory)
    with pytest.raises(ValueError):
        task_func(str(source_path / "file1.txt"), str(destination_path))

    # Test with invalid input (destination_path is not a directory)
    with pytest.raises(ValueError):
        task_func(str(source_path), str(destination_path / "file1.txt"))

    # Test with invalid input (source_path does not exist)
    with pytest.raises(ValueError):
        task_func(str(source_path / "nonexistent_dir"), str(destination_path))

    # Test with invalid input (destination_path does not exist)
    with pytest.raises(ValueError):
        task_func(str(source_path), str(destination_path / "nonexistent_dir"))