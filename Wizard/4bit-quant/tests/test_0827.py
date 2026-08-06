python
import os
import shutil
import re
import pytest

from src_0827 import task_func

def test_task_func():
    source_dir = "test_source_dir"
    target_dir = "test_target_dir"
    file_pattern = r'\b[A-Za-z0-9]+\.(txt|doc|docx)\b'

    # create source directory and files
    os.makedirs(source_dir)
    with open(os.path.join(source_dir, "file1.txt"), "w") as f:
        f.write("test")
    with open(os.path.join(source_dir, "file2.doc"), "w") as f:
        f.write("test")
    with open(os.path.join(source_dir, "file3.docx"), "w") as f:
        f.write("test")

    # test function with valid input
    assert task_func(source_dir, target_dir, file_pattern) == 3

    # test function with non-existent source directory
    with pytest.raises(FileNotFoundError):
        task_func("non_existent_dir", target_dir, file_pattern)

    # test function with non-existent target directory
    task_func(source_dir, "non_existent_dir", file_pattern)
    assert os.path.exists("non_existent_dir")

    # test function with invalid file pattern
    with pytest.raises(re.error):
        task_func(source_dir, target_dir, r'invalid_pattern')

    # test function with empty source directory
    os.rmdir(source_dir)
    assert task_func(source_dir, target_dir, file_pattern) == 0

    # test function with empty target directory
    os.makedirs(source_dir)
    os.rmdir(target_dir)
    assert task_func(source_dir, target_dir, file_pattern) == 0