import os
import pandas as pd
import re
import pytest
from src_0488 import task_func

def test_task_func():
    file_path = "path/to/log/file.log"
    expected_df = pd.DataFrame({
        "Timestamp": ["2023-01-01 12:00:00.000000", "2023-01-02 08:00:00.000000"],
        "Level": ["INFO", "ERROR"],
        "Message": ["Log message 1", "Log message 2"]
    })

    # Test if the function raises a FileNotFoundError if the file does not exist
    with pytest.raises(FileNotFoundError):
        task_func("path/to/nonexistent/file.log")

    # Test if the function returns the expected DataFrame when the file exists
    with open(file_path, "w") as f:
        f.write("2023-01-01 12:00:00.000000 - INFO - Log message 1n2023-01-02 08:00:00.000000 - ERROR - Log message 2n")
    actual_df = task_func(file_path)
    assert actual_df.equals(expected_df)

    # Test if the function returns an empty DataFrame if the log file is empty
    with open(file_path, "w") as f:
        f.write("")
    actual_df = task_func(file_path)
    assert actual_df.empty