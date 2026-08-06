import subprocess
import os
import glob
import pytest
from src_0786 import task_func

# Constants
ARCHIVE_DIR = '/tmp/archive'

def test_task_func():
    # Test with a valid pattern
    pattern = '/tmp/*.txt'
    archive_file = task_func(pattern)
    assert archive_file.startswith(ARCHIVE_DIR)
    assert archive_file.endswith('.tar.gz')
    assert os.path.exists(archive_file)

    # Test with an invalid pattern
    pattern = '/tmp/nonexistent/*.txt'
    archive_file = task_func(pattern)
    assert archive_file == "No files found matching the pattern."

def test_task_func_with_existing_archive_dir():
    # Create an existing archive directory
    os.makedirs(ARCHIVE_DIR)

    # Test with a valid pattern
    pattern = '/tmp/*.txt'
    archive_file = task_func(pattern)
    assert archive_file.startswith(ARCHIVE_DIR)
    assert archive_file.endswith('.tar.gz')
    assert os.path.exists(archive_file)

    # Clean up
    os.rmdir(ARCHIVE_DIR)

def test_task_func_with_existing_archive_files():
    # Create an existing archive directory
    os.makedirs(ARCHIVE_DIR)

    # Create some existing archive files
    archive_file_base = os.path.join(ARCHIVE_DIR, 'archive')
    for i in range(1, 4):
        archive_file = f"{archive_file_base}_{i}.tar.gz"
        with open(archive_file, 'w') as f:
            f.write('test')

    # Test with a valid pattern
    pattern = '/tmp/*.txt'
    archive_file = task_func(pattern)
    assert archive_file.startswith(ARCHIVE_DIR)
    assert archive_file.endswith('.tar.gz')
    assert os.path.exists(archive_file)
    assert os.path.basename(archive_file).startswith('archive_')

    # Clean up
    for i in range(1, 4):
        archive_file = f"{archive_file_base}_{i}.tar.gz"
        os.remove(archive_file)
    os.rmdir(ARCHIVE_DIR)