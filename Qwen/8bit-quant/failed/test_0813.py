import pytest
from src_0813 import task_func
from pathlib import Path
import tarfile
import re

# Mocking necessary modules and functions
class MockPath(Path):
    def rglob(self, pattern):
        return [MockPath('C:\\SomeDir\\AcroTray.exe'), MockPath('C:\\SomeDir\\Distillr\\AcroTray.exe')]

    def relative_to(self, other):
        return self - other

    def __sub__(self, other):
        return MockPath(str(self)[len(str(other)) + 1:])

    def __str__(self):
        return self._path

    def __init__(self, path):
        self._path = path

    def exists(self):
        return True

    def is_file(self):
        return True

class MockTarFile:
    def __init__(self, name, mode):
        self.name = name
        self.mode = mode
        self.added_files = []

    def add(self, path, arcname):
        self.added_files.append((path, arcname))

    def close(self):
        pass

def mock_open(name, mode):
    return MockTarFile(name, mode)

# Patching the necessary modules
@pytest.fixture(autouse=True)
def patch_modules(monkeypatch):
    monkeypatch.setattr(Path, '__new__', MockPath)
    monkeypatch.setattr(tarfile, 'open', mock_open)

def test_task_func():
    directory = r"C:\\SomeDir\\"
    file_pattern = r"(?<!Distillr)\\\\AcroTray\.exe"
    result = task_func(directory=directory, file_pattern=file_pattern)
    
    expected_tar_path = Path(directory) / 'archive.tar'
    assert result == str(expected_tar_path)
    
    # Check if the correct files were added to the tar archive
    tar_file = mock_open(str(expected_tar_path), 'w')
    assert len(tar_file.added_files) == 1
    assert tar_file.added_files[0] == (MockPath('C:\\SomeDir\\AcroTray.exe'), 'AcroTray.exe')

def test_task_func_with_permission_error(monkeypatch):
    def mock_add(self, path, arcname):
        raise PermissionError("Permission denied")

    monkeypatch.setattr(MockTarFile, 'add', mock_add)
    
    directory = r"C:\\SomeDir\\"
    file_pattern = r"(?<!Distillr)\\\\AcroTray\.exe"
    result = task_func(directory=directory, file_pattern=file_pattern)
    
    expected_tar_path = Path(directory) / 'archive.tar'
    assert result == str(expected_tar_path)
    
    # Check if the correct files were attempted to be added to the tar archive
    tar_file = mock_open(str(expected_tar_path), 'w')
    assert len(tar_file.added_files) == 1
    assert tar_file.added_files[0] == (MockPath('C:\\SomeDir\\AcroTray.exe'), 'AcroTray.exe')