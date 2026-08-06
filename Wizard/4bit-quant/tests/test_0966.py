python
import os
import re
import shutil
import pytest

from src_0966 import task_func

def test_task_func():
    # Test case 1: source directory does not exist
    with pytest.raises(FileNotFoundError):
        task_func("non_existent_dir", "target_dir")

    # Test case 2: source directory is not a directory
    with pytest.raises(NotADirectoryError):
        task_func("file.txt", "target_dir")

    # Test case 3: target directory does not exist
    os.makedirs("target_dir")
    assert task_func("source_dir", "target_dir") == 0

    # Test case 4: target directory is a file
    with pytest.raises(IsADirectoryError):
        task_func("source_dir", "target_dir/file.txt")

    # Test case 5: pattern is not a valid regex
    with pytest.raises(re.error):
        task_func("source_dir", "target_dir", pattern="[")

    # Test case 6: pattern matches no files
    os.makedirs("source_dir/subdir")
    with open("source_dir/file.txt", "w") as f:
        f.write("This is a test file.")
    assert task_func("source_dir", "target_dir", pattern="no_match") == 0

    # Test case 7: pattern matches some files
    os.makedirs("source_dir/subdir2")
    with open("source_dir/file1.txt", "w") as f:
        f.write("This is a test file.")
    with open("source_dir/file2.txt", "w") as f:
        f.write("This is a test file.")
    with open("source_dir/subdir/file3.txt", "w") as f:
        f.write("This is a test file.")
    with open("source_dir/subdir2/file4.txt", "w") as f:
        f.write("This is a test file.")
    assert task_func("source_dir", "target_dir", pattern=r"\d{4}") == 2

    # Test case 8: pattern matches all files
    os.makedirs("source_dir/subdir3")
    with open("source_dir/file5.txt", "w") as f:
        f.write("This is a test file.")
    with open("source_dir/file6.txt", "w") as f:
        f.write("This is a test file.")
    with open("source_dir/subdir/file7.txt", "w") as f:
        f.write("This is a test file.")
    with open("source_dir/subdir2/file8.txt", "w") as f:
        f.write("This is a test file.")
    with open("source_dir/subdir3/file9.txt", "w") as f:
        f.write("This is a test file.")
    assert task_func("source_dir", "target_dir", pattern=r"\d{4}") == 5