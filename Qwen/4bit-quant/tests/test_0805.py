import pytest
from src_0805 import task_func
import os
from datetime import datetime

def test_task_func_valid_input():
    metrics = {'accuracy': 0.9, 'loss': 0.1}
    filename = 'test_log.txt'
    result = task_func(metrics, filename)
    assert result is True
    log_path = os.path.join('./logs', filename)
    assert os.path.exists(log_path)
    with open(log_path, 'r') as f:
        lines = f.readlines()
        assert len(lines) > 3  # datetime + 2 metrics + newline
        assert lines[0].strip().startswith(str(datetime.now()))
        assert lines[1].strip() == 'accuracy: 0.9'
        assert lines[2].strip() == 'loss: 0.1'

def test_task_func_invalid_metrics_type():
    metrics = [1, 2, 3]
    filename = 'test_log.txt'
    with pytest.raises(ValueError) as excinfo:
        task_func(metrics, filename)
    assert str(excinfo.value) == "Metrics must be a dictionary"

def test_task_func_invalid_filename_type():
    metrics = {'accuracy': 0.9, 'loss': 0.1}
    filename = 123
    with pytest.raises(ValueError) as excinfo:
        task_func(metrics, filename)
    assert str(excinfo.value) == "Filename must be a string"

def test_task_func_write_failure(mocker):
    metrics = {'accuracy': 0.9, 'loss': 0.1}
    filename = 'test_log.txt'
    mocker.patch('src_0805.open', side_effect=IOError("Mocked IOError"))
    result = task_func(metrics, filename)
    assert result is False

def test_task_func_custom_log_dir():
    metrics = {'accuracy': 0.9, 'loss': 0.1}
    filename = 'test_log.txt'
    custom_log_dir = '/tmp/custom_logs'
    result = task_func(metrics, filename, log_dir=custom_log_dir)
    assert result is True
    log_path = os.path.join(custom_log_dir, filename)
    assert os.path.exists(log_path)