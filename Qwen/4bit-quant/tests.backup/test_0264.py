import pytest
from src_0264 import task_func
import os
import time
import tempfile
import shutil

@pytest.fixture
def setup_files(tmpdir):
    # Create temporary directory and files with different ages
    temp_dir = tmpdir.mkdir("temp")
    old_file = temp_dir.join("old_file.txt")
    old_file.write("This is an old file.")
    os.utime(old_file.strpath, (time.time() - 86401, time.time() - 86401))  # 1 day older than 1 day old

    recent_file = temp_dir.join("recent_file.txt")
    recent_file.write("This is a recent file.")
    os.utime(recent_file.strpath, (time.time() - 86399, time.time() - 86399))  # 1 second younger than 1 day old

    return temp_dir.strpath

def test_task_func(setup_files):
    my_path = setup_files
    days_old = 1
    archive_dir = task_func(my_path, days_old)

    # Check if the archive directory exists
    assert os.path.exists(archive_dir)

    # Check if the old file is moved to the archive directory
    assert not os.path.exists(os.path.join(my_path, "old_file.txt"))
    assert os.path.exists(os.path.join(archive_dir, "old_file.txt"))

    # Check if the recent file is not moved
    assert os.path.exists(os.path.join(my_path, "recent_file.txt"))

def test_task_func_no_files(setup_files):
    my_path = setup_files
    days_old = 10
    archive_dir = task_func(my_path, days_old)

    # Check if the archive directory exists
    assert os.path.exists(archive_dir)

    # Check if no files are moved since none are older than 10 days
    assert not os.path.exists(os.path.join(archive_dir, "old_file.txt"))
    assert os.path.exists(os.path.join(my_path, "old_file.txt"))

def test_task_func_empty_directory(tmpdir):
    empty_dir = tmpdir.mkdir("empty").strpath
    days_old = 1
    archive_dir = task_func(empty_dir, days_old)

    # Check if the archive directory exists
    assert os.path.exists(archive_dir)

    # Check if no files are moved since there are no files
    assert not os.listdir(archive_dir)