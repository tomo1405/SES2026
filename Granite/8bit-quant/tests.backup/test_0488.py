import os
import pandas as pd
import re
from src_0488 import task_func

def test_task_func_file_not_found():
    file_path = "path/to/nonexistent/file.txt"
    with pytest.raises(FileNotFoundError):
        task_func(file_path)

def test_task_func_valid_file():
    file_path = "path/to/valid/file.txt"
    with open(file_path, "w") as f:
        f.write("2022-01-01 12:00:00.000000 - INFO - This is a test message\n")
        f.write("2022-01-02 08:00:00.000000 - ERROR - This is another test message\n")
    df = task_func(file_path)
    expected_df = pd.DataFrame({
        "Timestamp": ["2022-01-01 12:00:00.000000", "2022-01-02 08:00:00.000000"],
        "Level": ["INFO", "ERROR"],
        "Message": ["This is a test message", "This is another test message"]
    })
    assert df.equals(expected_df)

def test_task_func_empty_file():
    file_path = "path/to/empty/file.txt"
    with open(file_path, "w") as f:
        pass
    df = task_func(file_path)
    expected_df = pd.DataFrame(columns=["Timestamp", "Level", "Message"])
    assert df.equals(expected_df)