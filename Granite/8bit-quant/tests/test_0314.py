import re
import os
import shutil
from datetime import datetime
from src_0314 import task_func
import pytest

def test_task_func():
    directory = "/path/to/directory"
    expected_directory = "/path/to/directory"
    expected_moved_files = {
        "subdirectory1": ["file1_20230101000000.txt", "file2_20230101000000.txt"],
        "subdirectory2": ["file3_20230101000000.txt"]
    }

    actual_directory, actual_moved_files = task_func(directory)

    assert actual_directory == expected_directory
    assert actual_moved_files == expected_moved_files