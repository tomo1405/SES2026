import os
import shutil
import pytest
from src_0119 import task_func

def test_task_func():
    directory = "/path/to/source/directory"
    backup_directory = "/path/to/backup/directory"
    copied_files = task_func(directory, backup_directory)

    assert len(copied_files) > 0
    for filename in copied_files:
        assert os.path.exists(filename)