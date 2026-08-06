import os
import pytest
from datetime import datetime
from src_0805 import task_func

LOG_DIR = './logs'

def test_task_func_valid_metrics():
    metrics = {'accuracy': 0.85, 'precision': 0.9, 'recall': 0.8}
    filename = 'test_metrics.log'
    result = task_func(metrics, filename, log_dir=LOG_DIR)
    assert result is True
    with open(os.path.join(LOG_DIR, filename), 'r') as f:
        lines = f.readlines()
        assert len(lines) == 4
        assert lines[0].startswith(str(datetime.now()))
        assert lines[1].startswith('accuracy: 0.85')
        assert lines[2].startswith('precision: 0.9')
        assert lines[3].startswith('recall: 0.8')

def test_task_func_invalid_metrics():
    metrics = 'invalid_metrics'
    filename = 'test_invalid_metrics.log'
    with pytest.raises(ValueError) as excinfo:
        task_func(metrics, filename, log_dir=LOG_DIR)
    assert "Metrics must be a dictionary" in str(excinfo.value)

def test_task_func_invalid_filename():
    metrics = {'accuracy': 0.85, 'precision': 0.9, 'recall': 0.8}
    filename = 123
    with pytest.raises(ValueError) as excinfo:
        task_func(metrics, filename, log_dir=LOG_DIR)
    assert "Filename must be a string" in str(excinfo.value)

def test_task_func_io_error():
    metrics = {'accuracy': 0.85, 'precision': 0.9, 'recall': 0.8}
    filename = 'test_io_error.log'
    log_dir = '/invalid/path'
    with pytest.raises(IOError) as excinfo:
        task_func(metrics, filename, log_dir=log_dir)
    assert "An error occurred" in str(excinfo.value)