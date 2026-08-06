import pytest
from src_0805 import task_func

# Test cases
def test_task_func_valid_input():
    metrics = {'metric1': 1, 'metric2': 2}
    filename = 'test_log.txt'
    result = task_func(metrics, filename)
    assert result is True

def test_task_func_invalid_metrics():
    metrics = "invalid metrics"
    filename = 'test_log.txt'
    with pytest.raises(ValueError):
        task_func(metrics, filename)

def test_task_func_invalid_filename():
    metrics = {'metric1': 1}
    filename = 123  # Invalid filename
    with pytest.raises(ValueError):
        task_func(metrics, filename)

def test_task_func_file_write_error():
    metrics = {'metric1': 1}
    filename = 'test_log.txt'
    with pytest.raises(Exception):
        task_func(metrics, filename)