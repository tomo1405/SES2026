import pytest
from src_0323 import task_func
import os
import shutil
import subprocess
import sys

# Mocking the required modules and functions
class MockSubprocessPopen:
    def __init__(self, *args, **kwargs):
        self.returncode = 0

    def poll(self):
        return self.returncode

class MockShutil:
    @staticmethod
    def copy(src, dst):
        pass

class MockOs:
    @staticmethod
    def path_join(dir, file):
        return f"{dir}\\{file}"

@pytest.fixture
def mock_modules(monkeypatch):
    monkeypatch.setattr(subprocess, 'Popen', MockSubprocessPopen)
    monkeypatch.setattr(shutil, 'copy', MockShutil.copy)
    monkeypatch.setattr(os, 'path', MockOs)

def test_task_func_success(mock_modules):
    filename = "test_file.txt"
    result = task_func(filename)
    assert result == 0

def test_task_func_backup_failure(mock_modules, monkeypatch):
    def mock_copy_failure(src, dst):
        raise Exception("Mocked copy failure")

    monkeypatch.setattr(shutil, 'copy', mock_copy_failure)
    filename = "test_file.txt"
    result = task_func(filename)
    assert result == -1

def test_task_func_execution_failure(mock_modules, monkeypatch):
    class MockSubprocessPopenFailure(MockSubprocessPopen):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.returncode = 1

    monkeypatch.setattr(subprocess, 'Popen', MockSubprocessPopenFailure)
    filename = "test_file.txt"
    result = task_func(filename)
    assert result == 1