import pytest
from src_0565 import task_func
import os
import ctypes
from datetime import datetime
import pytz
from unittest.mock import patch, MagicMock

# Mocking ctypes.CDLL and os.stat to avoid actual file system operations
class MockCDLL:
    def __init__(self, filepath):
        self.filepath = filepath
        self._name = "mock_lib_name"

class MockStatResult:
    def __init__(self, st_ctime, st_mtime, st_size):
        self.st_ctime = st_ctime
        self.st_mtime = st_mtime
        self.st_size = st_size

@patch('os.stat', return_value=MockStatResult(st_ctime=1633072800, st_mtime=1633072900, st_size=1024))
@patch('ctypes.CDLL', side_effect=MockCDLL)
def test_task_func(mock_cdll, mock_stat):
    filepath = "/path/to/mock/file"
    expected_lib_name = "mock_lib_name"
    expected_creation_time = datetime.fromtimestamp(1633072800, pytz.UTC)
    expected_modification_time = datetime.fromtimestamp(1633072900, pytz.UTC)
    expected_size = 1024
    expected_metadata = {
        'Creation Time': expected_creation_time,
        'Modification Time': expected_modification_time,
        'Size': expected_size
    }

    lib_name, metadata = task_func(filepath)

    assert lib_name == expected_lib_name
    assert metadata == expected_metadata

    mock_cdll.assert_called_once_with(filepath)
    mock_stat.assert_called_once_with(filepath)