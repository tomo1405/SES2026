import pytest
from src_0805 import task_func
import os
from datetime import datetime

def test_task_func_valid_input():
    metrics = {'accuracy': 0.95, 'loss': 0.02}
    filename = 'test_log.txt'
    log_dir = './logs'
    
    # Ensure the log directory exists
    os.makedirs(log_dir, exist_ok=True)
    
    result = task_func(metrics, filename, log_dir)
    assert result is True
    
    # Check if the file was created and contains the expected content
    with open(os.path.join(log_dir, filename), 'r') as f:
        lines = f.readlines()
    
    assert len(lines) >= 3  # At least timestamp, one metric, and a newline
    assert lines[0].strip().startswith(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    assert any('accuracy: 0.95' in line for line in lines)
    assert any('loss: 0.02' in line for line in lines)

def test_task_func_invalid_metrics_type():
    metrics = [1, 2, 3]
    filename = 'test_log.txt'
    log_dir = './logs'
    
    with pytest.raises(ValueError) as excinfo:
        task_func(metrics, filename, log_dir)
    
    assert "Metrics must be a dictionary" in str(excinfo.value)

def test_task_func_invalid_filename_type():
    metrics = {'accuracy': 0.95}
    filename = 12345
    log_dir = './logs'
    
    with pytest.raises(ValueError) as excinfo:
        task_func(metrics, filename, log_dir)
    
    assert "Filename must be a string" in str(excinfo.value)

def test_task_func_file_write_error():
    metrics = {'accuracy': 0.95}
    filename = 'test_log.txt'
    log_dir = '/nonexistent_directory'
    
    result = task_func(metrics, filename, log_dir)
    assert result is False