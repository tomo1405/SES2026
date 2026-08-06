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
    assert files_moved > 0

def test_task_func_no_files_moved():
    ROOT_DIR = 'path/to/root/dir'
    DEST_DIR = 'path/to/dest/dir'
    SPECIFIC_HASH = 'invalid_hash_value'
    files_moved = task_func(ROOT_DIR, DEST_DIR, SPECIFIC_HASH)
    assert files_moved == 0