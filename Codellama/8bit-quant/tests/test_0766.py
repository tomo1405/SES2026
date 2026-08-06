import pytest
from src_0766 import task_func

def test_task_func_with_valid_input():
    kwargs = {"file1.txt": "content1", "file2.txt": "content2"}
    target_dir = "non_none_files"
    copied_files = task_func(kwargs, target_dir)
    assert len(copied_files) == 2
    assert "file1.txt" in copied_files
    assert "file2.txt" in copied_files

def test_task_func_with_invalid_input():
    kwargs = {"file1.txt": "content1", "file2.txt": None}
    target_dir = "non_none_files"
    copied_files = task_func(kwargs, target_dir)
    assert len(copied_files) == 1
    assert "file1.txt" in copied_files
    assert "file2.txt" not in copied_files

def test_task_func_with_non_existent_file():
    kwargs = {"file1.txt": "content1", "file2.txt": "content2"}
    target_dir = "non_none_files"
    copied_files = task_func(kwargs, target_dir)
    assert len(copied_files) == 2
    assert "file1.txt" in copied_files
    assert "file2.txt" in copied_files

def test_task_func_with_existing_file():
    kwargs = {"file1.txt": "content1", "file2.txt": "content2"}
    target_dir = "non_none_files"
    copied_files = task_func(kwargs, target_dir)
    assert len(copied_files) == 2
    assert "file1.txt" in copied_files
    assert "file2.txt" in copied_files