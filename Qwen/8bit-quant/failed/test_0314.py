import pytest
from src_0314 import task_func
import os
import shutil
from datetime import datetime

# Helper function to create temporary files and directories
def setup_test_directory():
    test_dir = 'test_directory'
    os.makedirs(test_dir)
    with open(os.path.join(test_dir, 'file1.txt'), 'w') as f:
        f.write('example [subdir1]')
    with open(os.path.join(test_dir, 'file2.txt'), 'w') as f:
        f.write('example [subdir2]')
    return test_dir

# Helper function to clean up the temporary directory
def teardown_test_directory(test_dir):
    shutil.rmtree(test_dir)

def test_task_func():
    test_dir = setup_test_directory()
    try:
        result = task_func(test_dir)
        assert isinstance(result, tuple)
        assert len(result) == 2
        directory, moved_files = result
        assert directory == test_dir
        assert isinstance(moved_files, dict)
        assert len(moved_files) == 2
        assert 'subdir1' in moved_files
        assert 'subdir2' in moved_files
        for subdir in moved_files:
            for filename in moved_files[subdir]:
                assert os.path.exists(os.path.join(test_dir, subdir, filename))
    finally:
        teardown_test_directory(test_dir)