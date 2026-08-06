import pytest
from src_0972 import task_func

def test_task_func_valid_directory():
    directory_path = "path/to/directory"
    file_details = task_func(directory_path)
    assert file_details == [
        ("file1.txt", 100, "2022-01-01T00:00:00Z", "2022-01-01T00:00:00Z"),
        ("file2.txt", 200, "2022-01-01T00:00:00Z", "2022-01-01T00:00:00Z"),
        ("file3.txt", 300, "2022-01-01T00:00:00Z", "2022-01-01T00:00:00Z"),
    ]

def test_task_func_invalid_directory():
    directory_path = "path/to/invalid/directory"
    with pytest.raises(ValueError):
        task_func(directory_path)