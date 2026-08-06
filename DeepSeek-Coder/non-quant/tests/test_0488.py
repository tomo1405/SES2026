import pytest
from src_0488 import task_func
import os
import pandas as pd

def test_task_func_valid_file():
    # Create a temporary file for testing
    test_data = """2023-04-01 12:34:56.123456 - INFO - This is a test log message.
    2023-04-01 12:34:56.123457 - ERROR - Another log message."""
    test_file_path = "test_log.txt"
    with open(test_file_path, "w") as f:
        f.write(test_data)

    try:
        result = task_func(test_file_path)
        assert isinstance(result, pd.DataFrame)
        assert not result.empty
        assert list(result.columns) == ["Timestamp", "Level", "Message"]
    finally:
        os.remove(test_file_path)

def test_task_func_file_not_found():
    with pytest.raises(FileNotFoundError):
        task_func("nonexistent_file.txt")