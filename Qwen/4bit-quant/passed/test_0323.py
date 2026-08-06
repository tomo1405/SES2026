import pytest
from src_0323 import task_func
import os
import shutil
import subprocess
import sys
import tempfile

# Mocking dependencies
class MockShutil:
    @staticmethod
    def copy(src, dst):
        pass

class MockSubprocess:
    def __init__(self, *args, **kwargs):
        self.returncode = 0

    def poll(self):
        return self.returncode

@pytest.fixture
def mock_shutil(monkeypatch):
    monkeypatch.setattr(shutil, 'copy', MockShutil.copy)

@pytest.fixture
def mock_subprocess(monkeypatch):
    monkeypatch.setattr(subprocess, 'Popen', MockSubprocess)

@pytest.fixture
def setup_directories():
    temp_dir = tempfile.mkdtemp()
    temp_backup_dir = os.path.join(temp_dir, 'Backup')
    os.makedirs(temp_backup_dir)
    yield (temp_dir, temp_backup_dir)
    shutil.rmtree(temp_dir)

def test_task_func_success(setup_directories, mock_shutil, mock_subprocess):
    directory, backup_directory = setup_directories
    filename = 'test_file.txt'
    file_path = os.path.join(directory, filename)
    with open(file_path, 'w') as f:
        f.write('test content')

    result = task_func(filename)
    assert result == 0

def test_task_func_backup_failure(setup_directories, mock_shutil, mock_subprocess, monkeypatch):
    def mock_copy_fail(src, dst):
        raise FileNotFoundError("File not found")

    monkeypatch.setattr(shutil, 'copy', mock_copy_fail)

    directory, _ = setup_directories
    filename = 'test_file.txt'
    file_path = os.path.join(directory, filename)
    with open(file_path, 'w') as f:
        f.write('test content')

    result = task_func(filename)
    assert result == -1

def test_task_func_execution_failure(setup_directories, mock_shutil, mock_subprocess, monkeypatch):
    def mock_popen_fail(*args, **kwargs):
        process = MockSubprocess()
        process.returncode = -1
        return process

    monkeypatch.setattr(subprocess, 'Popen', mock_popen_fail)

    directory, _ = setup_directories
    filename = 'test_file.txt'
    file_path = os.path.join(directory, filename)
    with open(file_path, 'w') as f:
        f.write('test content')

    result = task_func(filename)
    assert result == -1