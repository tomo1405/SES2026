import pytest
from src_0805 import task_func

def test_task_func_valid_input():
    metrics = {'metric1': 10, 'metric2': 20}
    filename = 'test_log.txt'
    log_dir = './logs'
    assert task_func(metrics, filename, log_dir) == True

def test_task_func_invalid_metrics():
    metrics = 10
    filename = 'test_log.txt'
    log_dir = './logs'
    with pytest.raises(ValueError):
        task_func(metrics, filename, log_dir)

def test_task_func_invalid_filename():
    metrics = {'metric1': 10, 'metric2': 20}
    filename = 10
    log_dir = './logs'
    with pytest.raises(ValueError):
        task_func(metrics, filename, log_dir)

def test_task_func_invalid_log_dir():
    metrics = {'metric1': 10, 'metric2': 20}
    filename = 'test_log.txt'
    log_dir = 10
    with pytest.raises(ValueError):
        task_func(metrics, filename, log_dir)