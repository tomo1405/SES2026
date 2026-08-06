import pytest
from src_0162 import task_func
import os
import pandas as pd

@pytest.fixture
def create_log_file(tmpdir):
    log_content = """INFO: [ 2023-10-01 12:34:56 ] - This is an info message.
ERROR: [ 2023-10-01 12:35:00 ] - This is an error message.
INFO: [ 2023-10-01 12:35:05 ] - Another info message."""
    log_file = tmpdir.join("test_log.log")
    log_file.write(log_content)
    return str(log_file)

def test_task_func(create_log_file):
    output_path = task_func(create_log_file)
    assert os.path.exists(output_path)
    
    df = pd.read_csv(output_path)
    assert df.shape == (3, 3)
    assert df.columns.tolist() == ['Type', 'Timestamp', 'Message']
    
    expected_types = ['INFO', 'ERROR', 'INFO']
    expected_timestamps = ['2023-10-01 12:34:56', '2023-10-01 12:35:00', '2023-10-01 12:35:05']
    expected_messages = ['This is an info message.', 'This is an error message.', 'Another info message.']
    
    assert df['Type'].tolist() == expected_types
    assert df['Timestamp'].tolist() == expected_timestamps
    assert df['Message'].tolist() == expected_messages

def test_invalid_timestamp(create_log_file, tmpdir):
    invalid_log_content = """INFO: [ 2023-10-01 12:34:56 ] - This is an info message.
ERROR: [ 2023-10-01 12:35:00 ] - This is an error message.
INFO: [ 2023-10-01 12:35:05 ] - Another info message.
INFO: [ 2023-10-01 12:35:61 ] - Invalid timestamp."""
    invalid_log_file = tmpdir.join("invalid_log.log")
    invalid_log_file.write(invalid_log_content)
    
    with pytest.raises(ValueError) as excinfo:
        task_func(str(invalid_log_file))
    assert "Invalid timestamp format" in str(excinfo.value)

def test_no_valid_entries(create_log_file, tmpdir):
    empty_log_content = """DEBUG: [ 2023-10-01 12:34:56 ] - This is a debug message.
WARNING: [ 2023-10-01 12:35:00 ] - This is a warning message."""
    empty_log_file = tmpdir.join("empty_log.log")
    empty_log_file.write(empty_log_content)
    
    with pytest.raises(ValueError) as excinfo:
        task_func(str(empty_log_file))
    assert "No valid log entries found" in str(excinfo.value)