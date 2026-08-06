import pytest
from src_0369 import task_func

def test_task_func():
    # Testing with a valid source and destination directory
    src_dir = "path/to/src/dir"
    dest_dir = "path/to/dest/dir"
    file_name = task_func(src_dir, dest_dir)
    assert file_name == "file_name"

    # Testing with an invalid source directory
    src_dir = "path/to/invalid/src/dir"
    with pytest.raises(FileNotFoundError):
        task_func(src_dir, dest_dir)

    # Testing with an invalid destination directory
    dest_dir = "path/to/invalid/dest/dir"
    with pytest.raises(FileNotFoundError):
        task_func(src_dir, dest_dir)

    # Testing with a seed value
    seed = 100
    file_name = task_func(src_dir, dest_dir, seed)
    assert file_name == "file_name"