python
import os
import pandas as pd
import re
import pytest

from src_0488 import task_func

def test_task_func():
    # Test case 1: Valid file path
    file_path = "test_logs.txt"
    with open(file_path, "w") as f:
        f.write("2022-01-01 00:00:00.000000 - INFO - This is a test log message.\n")
        f.write("2022-01-01 00:00:01.000000 - ERROR - This is an error log message.\n")
    df = task_func(file_path)
    assert df.shape == (2, 3)
    assert df.iloc[0]["Timestamp"] == "2022-01-01 00:00:00.000000"
    assert df.iloc[0]["Level"] == "INFO"
    assert df.iloc[0]["Message"] == "This is a test log message."
    assert df.iloc[1]["Timestamp"] == "2022-01-01 00:00:01.000000"
    assert df.iloc[1]["Level"] == "ERROR"
    assert df.iloc[1]["Message"] == "This is an error log message."
    os.remove(file_path)

    # Test case 2: Invalid file path
    with pytest.raises(FileNotFoundError):
        task_func("invalid_file.txt")

    # Test case 3: Empty file
    file_path = "empty_file.txt"
    with open(file_path, "w") as f:
        pass
    df = task_func(file_path)
    assert df.shape == (0, 3)
    os.remove(file_path)