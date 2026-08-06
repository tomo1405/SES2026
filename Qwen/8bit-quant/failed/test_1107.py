import pytest
from src_1107 import task_func
from datetime import datetime
from pathlib import Path

# Mocking os.path.getctime and Path.exists to avoid actual file system access
class MockPath(Path):
    def exists(self):
        return True

def mock_getctime(file_path):
    # Return a fixed timestamp for testing purposes
    return 1633072800  # Corresponds to 2021-10-01 00:00:00

@pytest.fixture
def patch_os_path(monkeypatch):
    monkeypatch.setattr(os.path, 'getctime', mock_getctime)
    monkeypatch.setattr(Path, 'exists', MockPath.exists)

def test_task_func_with_valid_file(patch_os_path):
    file_path = "test_file.txt"
    expected_time = "2021-10-01 00:00:00"
    assert task_func(file_path) == expected_time

def test_task_func_with_nonexistent_file():
    file_path = "nonexistent_file.txt"
    with pytest.raises(FileNotFoundError) as excinfo:
        task_func(file_path)
    assert str(excinfo.value) == f"No such file or directory: '{file_path}'"