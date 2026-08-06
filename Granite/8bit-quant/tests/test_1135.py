import os

import pytest
from src_1135 import task_func


def test_task_func():
    source_dir = "source_directory"
    target_dir = "target_directory"
    prefix = "#Hash: "
    new_files = task_func(source_dir, target_dir, prefix)
    assert isinstance(new_files, list)
    for file_path in new_files:
        assert os.path.exists(file_path)
        with open(file_path, 'r') as infile:
            content = infile.read()
        assert content.startswith(prefix)
        assert len(content.splitlines()) == 2
        assert content.splitlines()[1]
def test_task_func_with_nonexistent_source_dir():
    source_dir = "nonexistent_directory"
    target_dir = "target_directory"
    prefix = "#Hash: "
    with pytest.raises(FileNotFoundError):
        task_func(source_dir, target_dir, prefix)
def test_task_func_with_nonexistent_target_dir():
    source_dir = "source_directory"
    target_dir = "nonexistent_directory"
    prefix = "#Hash: "
    new_files = task_func(source_dir, target_dir, prefix)
    assert isinstance(new_files, list)
    for file_path in new_files:
        assert os.path.exists(file_path)
        with open(file_path, 'r') as infile:
            content = infile.read()
        assert content.startswith(prefix)
        assert len(content.splitlines()) == 2
        assert content.splitlines()[1]