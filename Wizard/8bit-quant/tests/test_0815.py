python
import os
import shutil
import re
import pytest

from src_0815 import task_func

def test_task_func():
    source_dir = 'tests/test_data/source'
    target_dir = 'tests/test_data/target'
    file_pattern = r'\b[A-Za-z0-9]+\.(txt|doc|docx)\b'

    # Test case 1: source directory does not exist
    with pytest.raises(FileNotFoundError):
        task_func('tests/test_data/nonexistent_dir', target_dir, file_pattern)

    # Test case 2: target directory does not exist
    task_func(source_dir, 'tests/test_data/nonexistent_target_dir', file_pattern)
    assert os.path.exists('tests/test_data/nonexistent_target_dir')

    # Test case 3: move files
    moved_files_count = task_func(source_dir, target_dir, file_pattern)
    assert moved_files_count == 2
    assert os.path.exists(os.path.join(target_dir, 'file1.txt'))
    assert os.path.exists(os.path.join(target_dir, 'file2.docx'))

    # Test case 4: move no files
    moved_files_count = task_func(source_dir, target_dir, r'\b[A-Za-z0-9]+\.(csv|jpg)\b')
    assert moved_files_count == 0
    assert not os.path.exists(os.path.join(target_dir, 'file1.txt'))
    assert not os.path.exists(os.path.join(target_dir, 'file2.docx'))