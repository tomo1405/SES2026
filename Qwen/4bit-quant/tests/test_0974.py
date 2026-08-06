import pytest
from src_0974 import task_func
import os
import shutil

# Mocking shutil.disk_usage to avoid actual disk access
class MockDiskUsage:
    def __init__(self, total, used, free):
        self.total = total
        self.used = used
        self.free = free

def mock_disk_usage(path):
    # Example values for testing
    return MockDiskUsage(total=1000, used=500, free=500)

shutil.disk_usage = mock_disk_usage

def test_task_func_invalid_path():
    with pytest.raises(ValueError):
        task_func(None)

def test_task_func_non_string_path():
    with pytest.raises(ValueError):
        task_func(123)

def test_task_func_nonexistent_path():
    with pytest.raises(FileNotFoundError):
        task_func("/nonexistent/path")

def test_task_func_empty_path():
    with pytest.raises(ValueError):
        task_func("")

def test_task_func_valid_path():
    # Assuming '/valid/path' exists and has valid components
    expected_result = [
        ('valid', {'total': 1000, 'used': 500, 'free': 500}),
        ('path', {'total': 1000, 'used': 500, 'free': 500})
    ]
    assert task_func("/valid/path") == expected_result

def test_task_func_with_custom_delimiter():
    # Assuming '/valid|path' exists and has valid components
    expected_result = [
        ('valid', {'total': 1000, 'used': 500, 'free': 500}),
        ('path', {'total': 1000, 'used': 500, 'free': 500})
    ]
    assert task_func("/valid|path", delimiter="|") == expected_result

def test_task_func_invalid_components():
    with pytest.raises(ValueError):
        task_func("/valid//path")