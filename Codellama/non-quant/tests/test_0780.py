import os
import shutil

from src_0780 import task_func


def test_task_func_valid_directory():
    directory = "/tmp/test_dir"
    os.makedirs(directory)
    backup_dir, errors = task_func(directory)
    assert backup_dir == "/fake/backup/path"
    assert not errors
    shutil.rmtree(directory)


def test_task_func_invalid_directory():
    directory = "/tmp/test_dir"
    backup_dir, errors = task_func(directory)
    assert backup_dir is None
    assert len(errors) == 1
    assert errors[0] == f"Directory does not exist: {directory}"


def test_task_func_permission_denied():
    directory = "/tmp/test_dir"
    os.makedirs(directory)
    backup_dir, errors = task_func(directory)
    assert backup_dir == "/fake/backup/path"
    assert len(errors) == 1
    assert errors[0] == f"Permission denied: {e}"
    shutil.rmtree(directory)


def test_task_func_exception():
    directory = "/tmp/test_dir"
    os.makedirs(directory)
    backup_dir, errors = task_func(directory)
    assert backup_dir is None
    assert len(errors) == 1
    assert errors[0] == str(e)
    shutil.rmtree(directory)