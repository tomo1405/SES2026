import pytest
from src_0666 import task_func
import shutil
import os
import fnmatch
import itertools

def test_task_func():
    src_dir = "/path/to/source/directory"
    dst_dir = "/path/to/destination/directory"
    FILE_PATTERNS = ['*.txt', '*.docx']
    matching_files = list(itertools.chain.from_iterable(
        fnmatch.filter(os.listdir(src_dir), pattern) for pattern in FILE_PATTERNS))
    for filename in matching_files:
        shutil.copy2(os.path.join(src_dir, filename), dst_dir)
    result = task_func(src_dir, dst_dir)
    assert result == dst_dir