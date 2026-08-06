import pytest
from src_0162 import task_func
import os
import pandas as pd

@pytest.fixture
def create_log_file(tmpdir):
    log_content = """ERROR: [2023-01-01 12:00:00] - This is an error message.
INFO: [2023-01-02 13:00:00] - This is an info message."""
    log_file = tmpdir.join("test_log.log")
    log_file.write(log_content)
    return str(log_file)

def test_task_func(create_log_file):
    output_path = task_func(create_log_file)
    assert os.path.exists(output_path)
    df = pd.read_csv(output_path)
    assert df.shape == (2, 3)
    assert df.iloc[0]['Type'] == 'ERROR'
    assert df.iloc[0]['Timestamp'] == '2023-01-01 12:00:00'
    assert df.iloc[0]['Message'] == 'This is an error message.'
    assert df.iloc[1]['Type'] == 'INFO'
    assert df.iloc[1]['Timestamp'] == '2023-01-02 13:00:00'
    assert df.iloc[1]['Message'] == 'This is an info message.'

def test_task_func_invalid_timestamp(create_log_file):
    invalid_log_content = "ERROR: [2023-02-30 12:00:00] - Invalid date."
    with open(create_log_file, 'w') as file:
        file.write(invalid_log_content)
    with pytest.raises(ValueError, match="Invalid timestamp format"):
        task_func(create_log_file)

def test_task_func_no_valid_entries(create_log_file):
    empty_log_content = ""
    with open(create_log_file, 'w') as file:
        file.write(empty_log_content)
    with pytest.raises(ValueError, match="No valid log entries found."):
        task_func(create_log_file)