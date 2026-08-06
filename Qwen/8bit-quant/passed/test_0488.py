import pytest
from src_0488 import task_func
import pandas as pd
import os

def test_task_func_file_not_found():
    with pytest.raises(FileNotFoundError):
        task_func("non_existent_file.log")

def test_task_func_empty_file(tmp_path):
    file_path = tmp_path / "empty.log"
    file_path.touch()
    result_df = task_func(str(file_path))
    assert result_df.equals(pd.DataFrame(columns=["Timestamp", "Level", "Message"]))

def test_task_func_valid_logs(tmp_path):
    file_content = """2023-10-01 12:00:00.000000 - INFO - This is an info message
2023-10-01 12:01:00.000000 - ERROR - This is an error message"""
    file_path = tmp_path / "valid_logs.log"
    file_path.write_text(file_content)
    result_df = task_func(str(file_path))
    expected_df = pd.DataFrame({
        "Timestamp": ["2023-10-01 12:00:00.000000", "2023-10-01 12:01:00.000000"],
        "Level": ["INFO", "ERROR"],
        "Message": ["This is an info message", "This is an error message"]
    })
    assert result_df.equals(expected_df)

def test_task_func_invalid_logs(tmp_path):
    file_content = """Invalid log line
2023-10-01 12:01:00.000000 - ERROR - This is an error message"""
    file_path = tmp_path / "invalid_logs.log"
    file_path.write_text(file_content)
    result_df = task_func(str(file_path))
    expected_df = pd.DataFrame({
        "Timestamp": ["2023-10-01 12:01:00.000000"],
        "Level": ["ERROR"],
        "Message": ["This is an error message"]
    })
    assert result_df.equals(expected_df)