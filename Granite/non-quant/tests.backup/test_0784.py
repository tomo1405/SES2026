import os
import shutil
import pytest

def task_func(src_dir, dest_dir, extension):
    files_moved = 0

    for file_name in os.listdir(src_dir):
        if file_name.endswith(extension):
            shutil.move(os.path.join(src_dir, file_name), os.path.join(dest_dir, file_name))
            files_moved += 1

    return files_moved

def test_task_func():
    src_dir = "/path/to/source/directory"
    dest_dir = "/path/to/destination/directory"
    extension = ".txt"

    files_moved = task_func(src_dir, dest_dir, extension)

    assert files_moved > 0, "No files were moved"