import os
import shutil
import random
import pytest

from src_0369 import task_func

def test_task_func():
    src_dir = "/path/to/source/directory"
    dest_dir = "/path/to/destination/directory"
    seed = 100

    with pytest.raises(FileNotFoundError):
        task_func(src_dir, dest_dir, seed)

    src_dir = "/path/to/source/directory"
    dest_dir = "/path/to/destination/directory"
    seed = 100

    file_name = task_func(src_dir, dest_dir, seed)

    assert file_name in os.listdir(src_dir)
    assert file_name not in os.listdir(dest_dir)