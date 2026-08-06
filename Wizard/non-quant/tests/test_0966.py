python
import os
import re
import shutil
import pytest

from src_0966 import task_func

def test_task_func():
    # Test case 1: source directory does not exist
    assert task_func("nonexistent_dir", "target_dir") == 0

    # Test case 2: target directory does not exist
    os.makedirs("target_dir")
    assert task_func("source_dir", "target_dir") == 0

    # Test case 3: source directory contains no files
    os.makedirs("source_dir")
    assert task_func("source_dir", "target_dir") == 0

    # Test case 4: source directory contains files but no matching files
    os.makedirs("source_dir/subdir1")
    os.makedirs("source_dir/subdir2")
    open("source_dir/file1.txt", "w").close()
    open("source_dir/file2.txt", "w").close()
    assert task_func("source_dir", "target_dir") == 0

    # Test case 5: source directory contains files and matching files
    os.makedirs("source_dir/subdir1")
    os.makedirs("source_dir/subdir2")
    open("source_dir/file1.txt", "w").close()
    open("source_dir/file2.txt", "w").close()
    open("source_dir/subdir1/file3.txt", "w").close()
    open("source_dir/subdir2/file4.txt", "w").close()
    open("source_dir/subdir2/file5.txt", "w").close()
    open("source_dir/subdir2/file6.txt", "w").close()
    assert task_func("source_dir", "target_dir", r"\d{4}") == 2

    # Test case 6: source directory contains files and matching files but no target directory
    os.makedirs("source_dir/subdir1")
    os.makedirs("source_dir/subdir2")
    open("source_dir/file1.txt", "w").close()
    open("source_dir/file2.txt", "w").close()
    open("source_dir/subdir1/file3.txt", "w").close()
    open("source_dir/subdir2/file4.txt", "w").close()
    open("source_dir/subdir2/file5.txt", "w").close()
    open("source_dir/subdir2/file6.txt", "w").close()
    assert task_func("source_dir", "nonexistent_dir", r"\d{4}") == 2

    # Test case 7: source directory contains files and matching files but target directory is empty
    os.makedirs("source_dir/subdir1")
    os.makedirs("source_dir/subdir2")
    open("source_dir/file1.txt", "w").close()
    open("source_dir/file2.txt", "w").close()
    open("source_dir/subdir1/file3.txt", "w").close()
    open("source_dir/subdir2/file4.txt", "w").close()
    open("source_dir/subdir2/file5.txt", "w").close()
    open("source_dir/subdir2/file6.txt", "w").close()
    os.makedirs("target_dir")
    assert task_func("source_dir", "target_dir", r"\d{4}") == 2

    # Test case 8: source directory contains files and matching files but target directory is not empty
    os.makedirs("source_dir/subdir1")
    os.makedirs("source_dir/subdir2")
    open("source_dir/file1.txt", "w").close()
    open("source_dir/file2.txt", "w").close()
    open("source_dir/subdir1/file3.txt", "w").close()
    open("source_dir/subdir2/file4.txt", "w").close()
    open("source_dir/subdir2/file5.txt", "w").close()
    open("source_dir/subdir2/file6.txt", "w").close()
    os.makedirs("target_dir")
    open("target_dir/file1.txt", "w").close()
    open("target_dir/file2.txt", "w").close()
    assert task_func("source_dir", "target_dir", r"\d{4}") == 2