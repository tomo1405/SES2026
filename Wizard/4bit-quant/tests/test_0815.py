python
import os
import shutil
import re
import pytest

from src_0815 import task_func

def test_task_func():
    source_dir = "tests/test_data/source_dir"
    target_dir = "tests/test_data/target_dir"
    file_pattern = r'\b[A-Za-z0-9]+\.(txt|doc|docx)\b'

    # Test if source directory does not exist
    with pytest.raises(FileNotFoundError):
        task_func("non_existent_dir", target_dir, file_pattern)

    # Test if target directory does not exist
    os.makedirs(target_dir, exist_ok=True)
    assert task_func(source_dir, target_dir, file_pattern) == 0

    # Test if file pattern is valid
    with pytest.raises(re.error):
        task_func(source_dir, target_dir, r'invalid_pattern')

    # Test if file is moved successfully
    os.makedirs(source_dir, exist_ok=True)
    with open(os.path.join(source_dir, "test.txt"), "w") as f:
        f.write("test")
    assert task_func(source_dir, target_dir, file_pattern) == 1
    assert os.path.exists(os.path.join(target_dir, "test.txt"))

    # Test if multiple files are moved successfully
    os.makedirs(source_dir, exist_ok=True)
    with open(os.path.join(source_dir, "test1.txt"), "w") as f:
        f.write("test1")
    with open(os.path.join(source_dir, "test2.doc"), "w") as f:
        f.write("test2")
    assert task_func(source_dir, target_dir, file_pattern) == 2
    assert os.path.exists(os.path.join(target_dir, "test1.txt"))
    assert os.path.exists(os.path.join(target_dir, "test2.doc"))