import pytest
from src_0264 import task_func
import os
import glob
import shutil
import tempfile
import time

@pytest.fixture
def setup_files(tmpdir):
    # Create temporary directory and files with different extensions
    my_path = tmpdir.mkdir("test_dir")
    for ext in ['.txt', '.csv', '.xlsx', '.docx', '.pdf']:
        my_path.join(f"old_file{ext}").write("content")
        my_path.join(f"new_file{ext}").write("content")
    
    # Set modification times
    old_time = time.time() - 2 * 86400  # 2 days old
    new_time = time.time()  # current time
    for ext in ['.txt', '.csv', '.xlsx', '.docx', '.pdf']:
        os.utime(str(my_path.join(f"old_file{ext}")), (old_time, old_time))
        os.utime(str(my_path.join(f"new_file{ext}")), (new_time, new_time))
    
    return str(my_path)

def test_task_func(setup_files):
    my_path = setup_files
    days_old = 1
    
    archive_dir = task_func(my_path, days_old)
    
    # Check if archive directory exists
    assert os.path.exists(archive_dir)
    
    # Check if old files are moved to archive directory
    for ext in ['.txt', '.csv', '.xlsx', '.docx', '.pdf']:
        assert not os.path.exists(os.path.join(my_path, f"old_file{ext}"))
        assert os.path.exists(os.path.join(archive_dir, f"old_file{ext}"))
    
    # Check if new files are not moved
    for ext in ['.txt', '.csv', '.xlsx', '.docx', '.pdf']:
        assert os.path.exists(os.path.join(my_path, f"new_file{ext}"))
        assert not os.path.exists(os.path.join(archive_dir, f"new_file{ext}"))

def test_task_func_no_files(tmpdir):
    my_path = str(tmpdir.mkdir("empty_dir"))
    days_old = 1
    
    archive_dir = task_func(my_path, days_old)
    
    # Check if archive directory exists
    assert os.path.exists(archive_dir)
    
    # Check if no files are moved
    for ext in ['.txt', '.csv', '.xlsx', '.docx', '.pdf']:
        assert not os.listdir(os.path.join(archive_dir, f"*{ext}"))