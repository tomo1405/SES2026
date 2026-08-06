import pytest
from src_0565 import task_func
import os
import ctypes
from datetime import datetime
import pytz

# Mocking ctypes.CDLL and os.stat to avoid actual file operations
class MockCDLL:
    def __init__(self, filepath):
        self._name = "MockLibraryName"

class MockStatResult:
    def __init__(self, st_ctime, st_mtime, st_size):
        self.st_ctime = st_ctime
        self.st_mtime = st_mtime
        self.st_size = st_size

def mock_os_stat(filepath):
    # Example timestamps and size
    return MockStatResult(1633072800, 1633159200, 1024)

def test_task_func():
    # Patching os.stat and ctypes.CDLL
    with pytest.monkeypatch.context() as mp:
        mp.setattr(os, 'stat', mock_os_stat)
        mp.setattr(ctypes, 'CDLL', MockCDLL)

        # Example filepath
        filepath = "/path/to/mock/file"

        # Expected metadata
        expected_creation_time = datetime.fromtimestamp(1633072800, pytz.UTC)
        expected_modification_time = datetime.fromtimestamp(1633159200, pytz.UTC)
        expected_size = 1024
        expected_metadata = {
            'Creation Time': expected_creation_time,
            'Modification Time': expected_modification_time,
            'Size': expected_size
        }

        # Call the function
        result_lib_name, result_metadata = task_func(filepath)

        # Assertions
        assert result_lib_name == "MockLibraryName"
        assert result_metadata == expected_metadata

if __name__ == "__main__":
    pytest.main()