import pytest
from src_0307 import task_func
import os
import logging
import tempfile

# Mocking os module to avoid actual file operations
class MockOs:
    def __init__(self):
        self.files = []

    def path_exists(self, path):
        return path in self.files

    def listdir(self, path):
        return [f for f in self.files if f.startswith(path)]

    def remove(self, path):
        if path in self.files:
            self.files.remove(path)
        else:
            raise FileNotFoundError(f"No such file: '{path}'")

# Monkey patching os module
@pytest.fixture(autouse=True)
def mock_os():
    original_os = os
    mock_os_instance = MockOs()
    os.path.exists = mock_os_instance.path_exists
    os.listdir = mock_os_instance.listdir
    os.remove = mock_os_instance.remove
    yield
    os = original_os

# Monkey patching logging module to capture logs
@pytest.fixture
def caplog(caplog):
    caplog.set_level(logging.INFO)
    return caplog

def test_task_func_directory_not_found():
    with pytest.raises(FileNotFoundError) as excinfo:
        task_func("/nonexistent/directory")
    assert str(excinfo.value) == "Directory '/nonexistent/directory' does not exist."

def test_task_func_no_jquery_files():
    mock_os.files = ["/tmp/test_dir/file1.txt", "/tmp/test_dir/file2.js"]
    removed_files, removed_file_names = task_func("/tmp/test_dir")
    assert removed_files == 0
    assert removed_file_names == []
    assert "Removed jQuery file:" not in caplog.text

def test_task_func_with_jquery_files():
    mock_os.files = ["/tmp/test_dir/jquery1.js", "/tmp/test_dir/jquery2.js", "/tmp/test_dir/file3.txt"]
    removed_files, removed_file_names = task_func("/tmp/test_dir")
    assert removed_files == 2
    assert sorted(removed_file_names) == ["jquery1.js", "jquery2.js"]
    assert "Removed jQuery file: jquery1.js" in caplog.text
    assert "Removed jQuery file: jquery2.js" in caplog.text

def test_task_func_error_removing_file():
    mock_os.files = ["/tmp/test_dir/jquery1.js"]
    mock_os.remove = lambda path: raise Exception("Simulated error")
    with pytest.raises(Exception) as excinfo:
        task_func("/tmp/test_dir")
    assert str(excinfo.value) == "Simulated error"
    assert "Error while removing file jquery1.js: Simulated error" in caplog.text