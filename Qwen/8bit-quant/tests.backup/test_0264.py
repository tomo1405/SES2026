import pytest
from src_0264 import task_func
import os
import glob
import shutil
import time
from tempfile import TemporaryDirectory

@pytest.fixture
def setup_files(tmpdir):
    # Create some test files
    for ext in ['.txt', '.csv', '.xlsx', '.docx', '.pdf']:
        with open(os.path.join(tmpdir, f'test{ext}'), 'w') as f:
            f.write('test content')
    # Modify the modification time of one file to be older than 1 day
    old_file = os.path.join(tmpdir, 'test.txt')
    os.utime(old_file, (time.time() - 86401, time.time() - 86401))
    return tmpdir

def test_task_func(setup_files):
    my_path = setup_files
    days_old = 1
    archive_dir = task_func(str(my_path), days_old)
    
    # Check if the archive directory exists
    assert os.path.exists(archive_dir)
    
    # Check if the old file is moved to the archive directory
    assert not os.path.exists(os.path.join(my_path, 'test.txt'))
    assert os.path.exists(os.path.join(archive_dir, 'test.txt'))
    
    # Check if other files are not moved
    for ext in ['.csv', '.xlsx', '.docx', '.pdf']:
        assert os.path.exists(os.path.join(my_path, f'test{ext}'))

def test_task_func_no_files(setup_files):
    my_path = setup_files
    days_old = 365  # Set a very high number to ensure no files are older
    archive_dir = task_func(str(my_path), days_old)
    
    # Check if the archive directory exists
    assert os.path.exists(archive_dir)
    
    # Check if no files are moved to the archive directory
    for ext in FILE_EXTENSIONS:
        assert os.path.exists(os.path.join(my_path, f'test{ext}'))
        assert not os.path.exists(os.path.join(archive_dir, f'test{ext}'))