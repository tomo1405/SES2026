import os

import pytest
from src_0815 import task_func


def test_task_func_valid_input():
    source_dir = "test_source_dir"
    target_dir = "test_target_dir"
    file_pattern = r'\b[A-Za-z0-9]+\.(txt|doc|docx)\b'

    os.makedirs(source_dir)
    os.makedirs(target_dir)

    with open(os.path.join(source_dir, "test_file.txt"), "w") as f:
        f.write("test content")

    assert task_func(source_dir, target_dir, file_pattern) == 1

    assert os.path.exists(os.path.join(target_dir, "test_file.txt"))

def test_task_func_invalid_input():
    source_dir = "test_source_dir"
    target_dir = "test_target_dir"
    file_pattern = r'\b[A-Za-z0-9]+\.(txt|doc|docx)\b'

    os.makedirs(source_dir)
    os.makedirs(target_dir)

    with open(os.path.join(source_dir, "test_file.txt"), "w") as f:
        f.write("test content")

    with pytest.raises(FileNotFoundError):
        task_func("invalid_source_dir", target_dir, file_pattern)

    with pytest.raises(FileNotFoundError):
        task_func(source_dir, "invalid_target_dir", file_pattern)

    with pytest.raises(FileNotFoundError):
        task_func(source_dir, target_dir, "invalid_file_pattern")