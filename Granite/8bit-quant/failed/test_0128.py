import os
import shutil
import glob
import hashlib
import pytest
from src_0128 import task_func

def test_task_func():
    ROOT_DIR = 'path/to/root/dir'
    DEST_DIR = 'path/to/dest/dir'
    SPECIFIC_HASH = 'specific_hash_value'
    files_moved = task_func(ROOT_DIR, DEST_DIR, SPECIFIC_HASH)
    assert files_moved == expected_files_moved

def test_task_func_with_invalid_root_dir():
    with pytest.raises(FileNotFoundError):
        task_func('invalid_root_dir', 'path/to/dest/dir', 'specific_hash_value')

def test_task_func_with_invalid_dest_dir():
    with pytest.raises(FileNotFoundError):
        task_func('path/to/root/dir', 'invalid_dest_dir', 'specific_hash_value')

def test_task_func_with_invalid_specific_hash():
    with pytest.raises(ValueError):
        task_func('path/to/root/dir', 'path/to/dest/dir', 'invalid_specific_hash')