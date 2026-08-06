import os
import pytest
from datetime import datetime
from src_0805 import task_func

LOG_DIR = './logs'

def test_task_func_valid_input():
    metrics = {'accuracy': 0.85, 'precision': 0.90, 'recall': 0.80}
    filename = 'test_log.txt'
    expected_output = True
    actual_output = task_func(metrics, filename, log_dir=LOG_DIR)
    assert actual_output == expected_output

def test_task_func_invalid_metrics():
    metrics = 'invalid_input'
    filename = 'test_log.txt'
    with pytest.raises(ValueError) as excinfo:
        task_func(metrics, filename, log_dir=LOG_DIR)
    assert 'Metrics must be a dictionary' in str(excinfo.value)

def test_task_func_invalid_filename():
    metrics = {'accuracy': 0.85, 'precision': 0.90, 'recall': 0.80}
    filename = 123
    with pytest.raises(ValueError) as excinfo:
        task_func(metrics, filename, log_dir=LOG_DIR)
    assert 'Filename must be a string' in str(excinfo.value)

def test_task_func_io_error():
    metrics = {'accuracy': 0.85, 'precision': 0.90, 'recall': 0.80}
    filename = 'test_log.txt'
    expected_output = False
    os.chmod(os.path.join(LOG_DIR, filename), 0o444) # Set file permissions to read-only
    actual_output = task_func(metrics, filename, log_dir=LOG_DIR)
    assert actual_output == expected_output
    os.chmod(os.path.join(LOG_DIR, filename), 0o666) # Reset file permissions