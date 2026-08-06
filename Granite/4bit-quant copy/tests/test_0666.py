import shutil
import os
import fnmatch
import itertools
import pytest

def task_func(src_dir, dst_dir):
    FILE_PATTERNS = ['*.txt', '*.docx']
    # Find all matching files
    matching_files = list(itertools.chain.from_iterable(
        fnmatch.filter(os.listdir(src_dir), pattern) for pattern in FILE_PATTERNS))

    for filename in matching_files:
        shutil.copy2(os.path.join(src_dir, filename), dst_dir)

    return dst_dir

def test_task_func():
    src_dir = "/path/to/source/directory"
    dst_dir = "/path/to/destination/directory"
    expected_output = "/path/to/destination/directory"
    actual_output = task_func(src_dir, dst_dir)
    assert actual_output == expected_output, "Output does not match expected output"

if __name__ == "__main__":
    pytest.main()