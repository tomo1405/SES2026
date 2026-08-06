python
import os
import pandas as pd
import re
import pytest

def task_func(file_path: str) -> pd.DataFrame:
    LOG_REGEX = r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6}) - (\w+) - (.+)$"

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")

    logs = []
    with open(file_path, "r") as f:
        for line in f:
            match = re.match(LOG_REGEX, line)
            if match:
                timestamp, level, message = match.groups()
                logs.append([timestamp, level, message])

    df = pd.DataFrame(logs, columns=["Timestamp", "Level", "Message"])

    if df.empty:
        df = pd.DataFrame(columns=["Timestamp", "Level", "Message"])

    return df

def test_task_func():
    # Test case 1: Valid file path
    file_path = "test_file.txt"
    with open(file_path, "w") as f:
        f.write("2022-01-01 00:00:00.000000 - INFO - This is a test log message.\n")
        f.write("2022-01-01 00:00:01.000000 - ERROR - This is another test log message.\n")
    df = task_func(file_path)
    assert df.shape == (2, 3)
    assert df.iloc[0]["Level"] == "INFO"
    assert df.iloc[1]["Message"] == "This is another test log message."
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