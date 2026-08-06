import re
import os
import shutil
from src_0815 import task_func

def test_task_func_with_valid_input():
    source_dir = "source_directory"
    target_dir = "target_directory"
    moved_files_count = task_func(source_dir, target_dir)
    assert moved_files_count >= 0

def test_task_func_with_invalid_source_dir():
    source_dir = "invalid_source_directory"
    target_dir = "target_directory"
    with pytest.raises(FileNotFoundError):
        task_func(source_dir, target_dir)

def test_task_func_with_invalid_target_dir():
    source_dir = "source_directory"
    target_dir = "invalid_target_directory"
    moved_files_count = task_func(source_dir, target_dir)
    assert moved_files_count == 0

def test_task_func_with_valid_input_and_file_pattern():
    source_dir = "source_directory"
    target_dir = "target_directory"
    file_pattern = r'\b[A-Za-z0-9]+\.(txt|doc|docx)\b'
    moved_files_count = task_func(source_dir, target_dir, file_pattern)
    assert moved_files_count >= 0