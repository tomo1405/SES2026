import re
import os
import shutil
from src_0827 import task_func

def test_task_func():
    source_dir = "source_directory"
    target_dir = "target_directory"
    file_pattern = r'\b[A-Za-z0-9]+\.(txt|doc|docx)\b'
    moved_files_count = task_func(source_dir, target_dir, file_pattern)
    assert moved_files_count >= 0, "The moved_files_count should be greater than or equal to 0"
    assert os.path.exists(source_dir), "The source directory should still exist"
    assert os.path.exists(target_dir), "The target directory should still exist"