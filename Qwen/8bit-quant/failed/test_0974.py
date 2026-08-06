import pytest
from src_0974 import task_func
import os
import shutil
from unittest.mock import patch, MagicMock

@pytest.fixture
def mock_os_path_exists(monkeypatch):
    def mock_exists(path):
        return True
    monkeypatch.setattr(os.path, 'exists', mock_exists)

@pytest.fixture
def mock_shutil_disk_usage(monkeypatch):
    def mock_disk_usage(path):
        return MagicMock(total=1024, used=512, free=512)
    monkeypatch.setattr(shutil, 'disk_usage', mock_disk_usage)

def test_task_func_valid_path(mock_os_path_exists, mock_shutil_disk_usage):
    path = "/valid/path"
    expected_result = [
        ('valid', {'total': 1024, 'used': 512, 'free': 512}),
        ('path', {'total': 1024, 'used': 512, 'free': 512})
    ]
    assert task_func(path) == expected_result

def test_task_func_invalid_path():
    with pytest.raises(FileNotFoundError):
        task_func("/invalid/path")

def test_task_func_empty_path():
    with pytest.raises(ValueError):
        task_func("")

def test_task_func_non_string_path():
    with pytest.raises(ValueError):
        task_func(123)

def test_task_func_path_with_empty_components():
    with pytest.raises(ValueError):
        task_func("//empty//components//")

def test_task_func_custom_delimiter(mock_os_path_exists, mock_shutil_disk_usage):
    path = "C:\\valid\\path"
    expected_result = [
        ('C:', {'total': 1024, 'used': 512, 'free': 512}),
        ('valid', {'total': 1024, 'used': 512, 'free': 512}),
        ('path', {'total': 1024, 'used': 512, 'free': 512})
    ]
    assert task_func(path, delimiter="\\") == expected_result