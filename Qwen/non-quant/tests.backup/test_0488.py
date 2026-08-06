import pytest
from src_0488 import task_func
import os
import pandas as pd

# Mocking the os.path.exists function to simulate file existence
def mock_os_path_exists(path):
    if path == "existing_file.log":
        return True
    elif path == "non_existing_file.log":
        return False
    else:
        return False

# Mocking the open function to simulate file reading
class MockOpen:
    def __init__(self, content):
        self.content = content

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass

    def readlines(self):
        return self.content.splitlines()

@pytest.fixture
def patch_os_path_exists(monkeypatch):
    monkeypatch.setattr(os, 'path.exists', mock_os_path_exists)

@pytest.fixture
def patch_open(monkeypatch):
    def mock_open(path, mode='r'):
        if path == "existing_file.log":
            return MockOpen("2023-10-01 12:00:00.123456 - INFO - This is a log message.")
        else:
            raise FileNotFoundError(f"The file {path} does not exist.")
    monkeypatch.setattr('builtins.open', mock_open)

def test_task_func_existing_file(patch_os_path_exists, patch_open):
    result_df = task_func("existing_file.log")
    expected_df = pd.DataFrame({
        "Timestamp": ["2023-10-01 12:00:00.123456"],
        "Level": ["INFO"],
        "Message": ["This is a log message."]
    })
    pd.testing.assert_frame_equal(result_df, expected_df)

def test_task_func_non_existing_file(patch_os_path_exists):
    with pytest.raises(FileNotFoundError, match="The file non_existing_file.log does not exist."):
        task_func("non_existing_file.log")

def test_task_func_empty_log_file(patch_os_path_exists, patch_open):
    def mock_open(path, mode='r'):
        if path == "empty_file.log":
            return MockOpen("")
        else:
            raise FileNotFoundError(f"The file {path} does not exist.")
    monkeypatch.setattr('builtins.open', mock_open)
    
    result_df = task_func("empty_file.log")
    expected_df = pd.DataFrame(columns=["Timestamp", "Level", "Message"])
    pd.testing.assert_frame_equal(result_df, expected_df)