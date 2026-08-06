import os
import re
import shutil
import pytest
from src_0966 import task_func

def test_task_func():
    source_directory = "source"
    target_directory = "target"
    pattern = r"\d{4}"
    moved_files_count = task_func(source_directory, target_directory, pattern)
    assert isinstance(moved_files_count, int)
    assert moved_files_count >= 0
    assert os.path.exists(target_directory)
    assert os.path.isdir(target_directory)
    for root, _, files in os.walk(source_directory):
        for file in files:
            if re.search(pattern, file):
                assert os.path.exists(os.path.join(target_directory, file))
                assert not os.path.exists(os.path.join(root, file))