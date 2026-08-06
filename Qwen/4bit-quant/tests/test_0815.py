import os
import shutil

import pytest
from src_0815 import task_func


def test_task_func_source_dir_not_exists():
    with pytest.raises(FileNotFoundError, match="The source directory does not exist."):
        task_func('/non/existing/source', '/target')

def test_task_func_target_dir_created():
    temp_dir = 'temp_test_dir'
    try:
        task_func('tests/data/source', temp_dir)
        assert os.path.exists(temp_dir)
    finally:
        shutil.rmtree(temp_dir)

def test_task_func_move_files():
    temp_dir = 'temp_test_dir'
    try:
        moved_count = task_func('tests/data/source', temp_dir)
        assert moved_count == 2
        assert os.path.exists(os.path.join(temp_dir, 'example.txt'))
        assert os.path.exists(os.path.join(temp_dir, 'document.docx'))
    finally:
        shutil.rmtree(temp_dir)

def test_task_func_no_files_match():
    temp_dir = 'temp_test_dir'
    try:
        moved_count = task_func('tests/data/source_empty', temp_dir)
        assert moved_count == 0
        assert not os.path.exists(os.path.join(temp_dir, 'nonexistent.txt'))
    finally:
        shutil.rmtree(temp_dir)