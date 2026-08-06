import re
import os
import shutil
from src_0827 import task_func

def test_task_func():
    source_dir = "source_directory"
    target_dir = "target_directory"
    file_pattern = r'\b[A-Za-z0-9]+\.(txt|doc|docx)\b'
    moved_files_count = task_func(source_dir, target_dir, file_pattern)
    assert moved_files_count >= 0

def test_task_func_file_not_found_error():
    source_dir = "non_existent_directory"
    target_dir = "target_directory"
    file_pattern = r'\b[A-Za-z0-9]+\.(txt|doc|docx)\b'
    try:
        task_func(source_dir, target_dir, file_pattern)
    except FileNotFoundError as e:
        assert str(e) == "The source directory does not exist."

def test_task_func_makedirs():
    source_dir = "source_directory"
    target_dir = "non_existent_directory"
    file_pattern = r'\b[A-Za-z0-9]+\.(txt|doc|docx)\b'
    moved_files_count = task_func(source_dir, target_dir, file_pattern)
    assert moved_files_count == 0

def test_task_func_ moved_files_count():
    source_dir = "source_directory"
    target_dir = "target_directory"
    file_pattern = r'\b[A-Za-z0-9]+\.(txt|doc|docx)\b'
    moved_files_count = task_func(source_dir, target_dir, file_pattern)
    assert moved_files_count >= 0