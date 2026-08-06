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

    # Test case 3: source directory contains no files matching pattern
    os.makedirs("source_dir")
    assert task_func("source_dir", "target_dir") == 0

    # Test case 4: source directory contains one file matching pattern
    os.makedirs("source_dir/subdir")
    with open("source_dir/file.txt", "w") as f:
        f.write("2021")
    assert task_func("source_dir", "target_dir") == 1

    # Test case 5: source directory contains multiple files matching pattern
    os.makedirs("source_dir/subdir2")
    with open("source_dir/file2.txt", "w") as f:
        f.write("2021")
    with open("source_dir/subdir/file3.txt", "w") as f:
        f.write("2021")
    assert task_func("source_dir", "target_dir") == 2

    # Test case 6: source directory contains files matching pattern in subdirectories
    os.makedirs("source_dir/subdir3/subdir4")
    with open("source_dir/subdir3/file4.txt", "w") as f:
        f.write("2021")
    with open("source_dir/subdir3/subdir4/file5.txt", "w") as f:
        f.write("2021")
    assert task_func("source_dir", "target_dir") == 4

    # Test case 7: source directory contains files matching pattern in multiple subdirectories
    os.makedirs("source_dir/subdir5/subdir6")
    with open("source_dir/subdir5/file6.txt", "w") as f:
        f.write("2021")
    with open("source_dir/subdir5/subdir6/file7.txt", "w") as f:
        f.write("2021")
    with open("source_dir/subdir3/file4.txt", "w") as f:
        f.write("2021")
    with open("source_dir/subdir3/subdir4/file5.txt", "w") as f:
        f.write("2021")
    assert task_func("source_dir", "target_dir") == 6

    # Test case 8: source directory contains files matching pattern in multiple subdirectories with different patterns
    os.makedirs("source_dir/subdir7/subdir8")
    with open("source_dir/subdir7/file8.txt", "w") as f:
        f.write("2021")
    with open("source_dir/subdir7/subdir8/file9.txt", "w") as f:
        f.write("2021")
    with open("source_dir/subdir3/file4.txt", "w") as f:
        f.write("2021")
    with open("source_dir/subdir3/subdir4/file5.txt", "w") as f:
        f.write("2021")
    with open("source_dir/subdir5/file6.txt", "w") as f:
        f.write("2021")
    with open("source_dir/subdir5/subdir6/file7.txt", "w") as f:
        f.write("2021")
    assert task_func("source_dir", "target_dir", pattern=r"\d{2}") == 4

    # Test case 9: source directory contains files matching pattern in multiple subdirectories with different patterns
    os.makedirs("source_dir/subdir9/subdir10")
    with open("source_dir/subdir9/file10.txt", "w") as f:
        f.write("2021")
    with open("source_dir/subdir9/subdir10/file11.txt", "w") as f:
        f.write("2021")
    with open("source_dir/subdir3/file4.txt", "w") as f:
        f.write("2021")
    with open("source_dir/subdir3/subdir4/file5.txt", "w") as f:
        f.write("2021")
    with open("source_dir/subdir5/file6.txt", "w") as f:
        f.write("2021")
    with open("source_dir/subdir5/subdir6/file7.txt", "w") as f:
        f.write("2021")
    assert task_func("source_dir", "target_dir", pattern=r"\d{3}") == 2