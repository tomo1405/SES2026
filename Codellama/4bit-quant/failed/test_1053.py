import pytest
from src_1053 import task_func

def test_task_func():
    # Test with a valid file path
    file_path = "path/to/file.csv"
    save_path = "path/to/save.png"
    ax = task_func(file_path, save_path)
    assert ax is not None

    # Test with an invalid file path
    file_path = "path/to/invalid/file.csv"
    save_path = "path/to/save.png"
    ax = task_func(file_path, save_path)
    assert ax is None

    # Test with a valid file path and no save path
    file_path = "path/to/file.csv"
    save_path = None
    ax = task_func(file_path, save_path)
    assert ax is not None

    # Test with an invalid file path and no save path
    file_path = "path/to/invalid/file.csv"
    save_path = None
    ax = task_func(file_path, save_path)
    assert ax is None