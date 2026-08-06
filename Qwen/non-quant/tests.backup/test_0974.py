import pytest
from src_0974 import task_func
import os
import shutil

# Mocking shutil.disk_usage to avoid system calls during tests
class MockDiskUsage:
    def __init__(self, total, used, free):
        self.total = total
        self.used = used
        self.free = free

def mock_disk_usage(path):
    # Simple mock based on the path length for demonstration purposes
    return MockDiskUsage(total=len(path) * 1024, used=len(path) * 512, free=len(path) * 512)

shutil.disk_usage = mock_disk_usage

def test_task_func_valid_path():
    path = "/home/user"
    expected_result = [
        ("home", {"total": 6*1024, "used": 6*512, "free": 6*512}),
        ("user", {"total": 11*1024, "used": 11*512, "free": 11*512})
    ]
    assert task_func(path) == expected_result

def test_task_func_invalid_path():
    with pytest.raises(FileNotFoundError):
        task_func("/nonexistent/path")

def test_task_func_empty_path():
    with pytest.raises(ValueError):
        task_func("")

def test_task_func_non_string_path():
    with pytest.raises(ValueError):
        task_func(123)

def test_task_func_path_with_invalid_components():
    with pytest.raises(ValueError):
        task_func("/home//user")

def test_task_func_single_component_path():
    path = "/root"
    expected_result = [("root", {"total": 5*1024, "used": 5*512, "free": 5*512})]
    assert task_func(path) == expected_result

def test_task_func_custom_delimiter():
    path = "C:\\Users\\Admin"
    expected_result = [
        ("C:", {"total": 3*1024, "used": 3*512, "free": 3*512}),
        ("Users", {"total": 8*1024, "used": 8*512, "free": 8*512}),
        ("Admin", {"total": 11*1024, "used": 11*512, "free": 11*512})
    ]
    assert task_func(path, delimiter="\\") == expected_result