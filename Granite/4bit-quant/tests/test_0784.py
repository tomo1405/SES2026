import os
import shutil
import pytest

from src_0784 import task_func

def test_task_func():
    src_dir = "/path/to/source/directory"
    dest_dir = "/path/to/destination/directory"
    extension = ".txt"

    files_moved = task_func(src_dir, dest_dir, extension)

    assert files_moved == 2
    assert os.path.exists(os.path.join(src_dir, "file1.txt")) is False
    assert os.path.exists(os.path.join(src_dir, "file2.txt")) is False
    assert os.path.exists(os.path.join(dest_dir, "file1.txt")) is True
    assert os.path.exists(os.path.join(dest_dir, "file2.txt")) is True