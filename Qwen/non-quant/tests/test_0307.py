import pytest
from src_0307 import task_func
import os
import logging
import tempfile

# Mocking os functions to avoid real file system operations
class MockOsModule:
    def __init__(self, directory_structure):
        self.directory_structure = directory_structure

    def path(self):
        return self

    def path_exists(self, path):
        return path in self.directory_structure

    def listdir(self, path):
        return self.directory_structure.get(path, [])

    def remove(self, path):
        if path in self.directory_structure:
            del self.directory_structure[path]
        else:
            raise FileNotFoundError(f"File '{path}' does not exist.")

@pytest.fixture
def mock_os():
    return MockOsModule({
        '/test_dir': ['jquery-1.js', 'script.js', 'jquery-2.js', 'style.css']
    })

@pytest.fixture(autouse=True)
def setup_logging():
    logging.basicConfig(level=logging.DEBUG)
    yield
    logging.shutdown()

def test_task_func(mock_os, monkeypatch):
    monkeypatch.setattr(os, 'path', mock_os.path)
    monkeypatch.setattr(os, 'exists', mock_os.path_exists)
    monkeypatch.setattr(os, 'listdir', mock_os.listdir)
    monkeypatch.setattr(os, 'remove', mock_os.remove)

    directory = '/test_dir'
    removed_files, removed_file_names = task_func(directory)

    assert removed_files == 2
    assert sorted(removed_file_names) == ['jquery-1.js', 'jquery-2.js']
    assert mock_os.directory_structure.get('/test_dir', []) == ['script.js', 'style.css']

def test_task_func_nonexistent_directory(monkeypatch):
    def mock_exists(path):
        return False

    monkeypatch.setattr(os, 'exists', mock_exists)

    with pytest.raises(FileNotFoundError, match="Directory '/nonexistent_dir' does not exist."):
        task_func('/nonexistent_dir')