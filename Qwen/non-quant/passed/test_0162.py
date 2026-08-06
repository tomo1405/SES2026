import pytest
from src_0162 import task_func
import os
import pandas as pd

@pytest.fixture
def create_log_file(tmpdir):
    log_content = """ERROR: [ 2023-01-01 12:00:00 ] - Error occurred
INFO: [ 2023-01-01 12:01:00 ] - Info message
"""
    log_file = tmpdir.join("test_log.log")
    log_file.write(log_content)
    return str(log_file)

def test_task_func(create_log_file):
    output_path = task_func(create_log_file)
    assert os.path.exists(output_path)
    df = pd.read_csv(output_path)
    assert df.equals(pd.DataFrame({
        'Type': ['ERROR', 'INFO'],
        'Timestamp': ['2023-01-01 12:00:00', '2023-01-01 12:01:00'],
        'Message': ['Error occurred', 'Info message']
    }))

def test_task_func_invalid_timestamp(create_log_file):
    invalid_log_content = """ERROR: [ 2023-01-01 12:00:60 ] - Error occurred"""
    with open(create_log_file, 'w') as file:
        file.write(invalid_log_content)
    
    with pytest.raises(ValueError, match="Invalid timestamp format: 2023-01-01 12:00:60"):
        task_func(create_log_file)

def test_task_func_no_valid_entries(create_log_file):
    empty_log_content = ""
    with open(create_log_file, 'w') as file:
        file.write(empty_log_content)
    
    with pytest.raises(ValueError, match="No valid log entries found."):
        task_func(create_log_file)