import os
import pandas as pd
import re
import pytest

from src_0488 import task_func

def test_task_func():
    file_path = "path/to/test/file.txt"
    expected_df = pd.DataFrame({
        "Timestamp": ["2023-01-01 12:00:00.000000", "2023-01-02 08:30:00.000000"],
        "Level": ["INFO", "ERROR"],
        "Message": ["File opened successfully", "Failed to read file"]
    })

    with open(file_path, "w") as f:
        f.write("2023-01-01 12:00:00.000000 - INFO - File opened successfully\n")
        f.write("2023-01-02 08:30:00.000000 - ERROR - Failed to read file\n")

    df = task_func(file_path)

    assert df.equals(expected_df)

def test_task_func_file_not_found():
    file_path = "path/to/nonexistent/file.txt"

    with pytest.raises(FileNotFoundError):
        task_func(file_path)