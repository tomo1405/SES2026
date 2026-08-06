import pytest
from src_0780 import task_func
import os
import shutil

# Mocking functions and constants
BACKUP_DIR = '/tmp/backup'

def mock_get_unique_backup_dir():
    return "/fake/backup/path"

@pytest.fixture
def setup_directories(tmpdir):
    original_dir = tmpdir.mkdir("original")
    backup_dir = tmpdir.mkdir("backup")
    return str(original_dir), str(backup_dir)

def test_task_func_directory_exists(setup_directories):
    original_dir, _ = setup_directories
    result, errors = task_func(original_dir)
    assert result == "/fake/backup/path"
    assert not errors

def test_task_func_directory_does_not_exist():
    non_existent_dir = "/path/to/nonexistent/directory"
    result, errors = task_func(non_existent_dir)
    assert result is None
    assert len(errors) == 1
    assert errors[0] == f"Directory does not exist: {non_existent_dir}"

def test_task_func_permission_error(monkeypatch, setup_directories):
    original_dir, _ = setup_directories
    monkeypatch.setattr(shutil, 'rmtree', lambda x: raise PermissionError("Mocked permission error"))
    result, errors = task_func(original_dir)
    assert result == "/fake/backup/path"
    assert len(errors) == 1
    assert "Permission denied: Mocked permission error" in errors[0]

def test_task_func_general_exception(monkeypatch, setup_directories):
    original_dir, _ = setup_directories
    monkeypatch.setattr(shutil, 'copytree', lambda x, y: raise Exception("Mocked general exception"))
    result, errors = task_func(original_dir)
    assert result is None
    assert len(errors) == 1
    assert "Mocked general exception" in errors[0]

def test_task_func_backup_dir_creation_failure(monkeypatch, setup_directories):
    original_dir, _ = setup_directories
    monkeypatch.setattr(os, 'makedirs', lambda x: raise Exception("Mocked makedirs failure"))
    result, errors = task_func(original_dir)
    assert result is None
    assert len(errors) == 1
    assert "Mocked makedirs failure" in errors[0]