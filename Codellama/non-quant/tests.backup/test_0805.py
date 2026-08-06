import pytest
from src_0805 import task_func

def test_task_func_valid_input():
    metrics = {'metric1': 1, 'metric2': 2}
    filename = 'test_file.txt'
    log_dir = './logs'
    assert task_func(metrics, filename, log_dir) == True

def test_task_func_invalid_metrics():
    metrics = 123
    filename = 'test_file.txt'
    log_dir = './logs'
    with pytest.raises(ValueError):
        task_func(metrics, filename, log_dir)

def test_task_func_invalid_filename():
    metrics = {'metric1': 1, 'metric2': 2}
    filename = 123
    log_dir = './logs'
    with pytest.raises(ValueError):
        task_func(metrics, filename, log_dir)

def test_task_func_invalid_log_dir():
    metrics = {'metric1': 1, 'metric2': 2}
    filename = 'test_file.txt'
    log_dir = 123
    with pytest.raises(ValueError):
        task_func(metrics, filename, log_dir)

def test_task_func_exception():
    metrics = {'metric1': 1, 'metric2': 2}
    filename = 'test_file.txt'
    log_dir = './logs'
    with pytest.raises(Exception):
        task_func(metrics, filename, log_dir)