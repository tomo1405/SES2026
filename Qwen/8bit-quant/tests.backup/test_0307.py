import pytest
from src_0307 import task_func
import os
import logging
import tempfile

# Mocking os.path.exists to control directory existence
def mock_os_path_exists(path):
    return path == '/mock/directory'

# Mocking os.listdir to simulate directory contents
def mock_os_listdir(path):
    return ['jquery.js', 'main.js', 'script.jquery.js', 'other.js']

# Mocking os.remove to simulate file removal
def mock_os_remove(path):
    pass

@pytest.fixture(autouse=True)
def setup():
    # Redirect logging to a temporary file
    log_file = tempfile.NamedTemporaryFile(delete=False)
    logging.basicConfig(filename=log_file.name, level=logging.INFO, 
                        format='%(asctime)s - %(levelname)s - %(message)s')
    yield
    log_file.close()
    os.unlink(log_file.name)

def test_task_func_directory_not_exists(monkeypatch):
    monkeypatch.setattr(os.path, 'exists', lambda x: False)
    with pytest.raises(FileNotFoundError) as excinfo:
        task_func('/nonexistent/directory')
    assert str(excinfo.value) == "Directory '/nonexistent/directory' does not exist."

def test_task_func_no_jquery_files(monkeypatch):
    monkeypatch.setattr(os.path, 'exists', mock_os_path_exists)
    monkeypatch.setattr(os.listdir, mock_os_listdir)
    result = task_func('/mock/directory')
    assert result == (0, [])

def test_task_func_with_jquery_files(monkeypatch):
    monkeypatch.setattr(os.path, 'exists', mock_os_path_exists)
    monkeypatch.setattr(os.listdir, mock_os_listdir)
    monkeypatch.setattr(os, 'remove', mock_os_remove)
    result = task_func('/mock/directory')
    assert result == (2, ['jquery.js', 'script.jquery.js'])

def test_task_func_logging(monkeypatch, caplog):
    monkeypatch.setattr(os.path, 'exists', mock_os_path_exists)
    monkeypatch.setattr(os.listdir, mock_os_listdir)
    monkeypatch.setattr(os, 'remove', mock_os_remove)
    task_func('/mock/directory')
    assert "Removed jQuery file: jquery.js" in caplog.text
    assert "Removed jQuery file: script.jquery.js" in caplog.text