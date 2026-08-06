import pytest
from src_0488 import task_func
import pandas as pd

def test_task_func_file_not_found():
    with pytest.raises(FileNotFoundError):
        task_func("non_existent_file.log")

def test_task_func_empty_log_file(tmp_path):
    empty_file = tmp_path / "empty_log.log"
    empty_file.write_text("")
    
    result_df = task_func(str(empty_file))
    assert result_df.equals(pd.DataFrame(columns=["Timestamp", "Level", "Message"]))

def test_task_func_valid_log_file(tmp_path):
    log_content = """2023-01-01 00:00:00.000000 - INFO - This is an info message
2023-01-01 00:01:00.000000 - ERROR - This is an error message"""
    log_file = tmp_path / "valid_log.log"
    log_file.write_text(log_content)
    
    result_df = task_func(str(log_file))
    expected_df = pd.DataFrame(
        [
            ["2023-01-01 00:00:00.000000", "INFO", "This is an info message"],
            ["2023-01-01 00:01:00.000000", "ERROR", "This is an error message"]
        ],
        columns=["Timestamp", "Level", "Message"]
    )
    assert result_df.equals(expected_df)

def test_task_func_invalid_log_format(tmp_path):
    invalid_log_content = """2023-01-01 00:00:00.000000 - INFO - This is an info message
invalid log line"""
    log_file = tmp_path / "invalid_log.log"
    log_file.write_text(invalid_log_content)
    
    result_df = task_func(str(log_file))
    expected_df = pd.DataFrame(
        [
            ["2023-01-01 00:00:00.000000", "INFO", "This is an info message"]
        ],
        columns=["Timestamp", "Level", "Message"]
    )
    assert result_df.equals(expected_df)