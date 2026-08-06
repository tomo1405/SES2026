import os
import shutil
from src_0780 import task_func

def test_task_func_valid_directory():
    directory = "/fake/directory"
    backup_dir, errors = task_func(directory)
    assert backup_dir == "/fake/backup/path"
    assert len(errors) == 0

def test_task_func_invalid_directory():
    directory = "/nonexistent/directory"
    backup_dir, errors = task_func(directory)
    assert backup_dir is None
    assert len(errors) == 2
    assert errors[0] == "Directory does not exist: /nonexistent/directory"
    assert errors[1] == "Directory does not exist: /nonexistent/directory"

def test_task_func_backup_error():
    directory = "/fake/directory"
    backup_dir = "/fake/backup/path"
    shutil.rmtree = lambda *args: raise Exception("Mock error")
    backup_dir, errors = task_func(directory)
    assert backup_dir is None
    assert len(errors) == 1
    assert errors[0] == "Mock error"