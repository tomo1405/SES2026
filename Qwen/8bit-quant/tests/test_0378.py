import pytest
from src_0378 import task_func
from unittest.mock import patch

def test_task_func_cpu_usage():
    with patch('psutil.cpu_percent') as mock_cpu_percent:
        mock_cpu_percent.return_value = 50
        result = task_func()
        assert 'CPU Usage (%)' in result
        assert '50' in result

def test_task_func_memory_usage():
    with patch('psutil.virtual_memory') as mock_virtual_memory:
        mock_virtual_memory.return_value = type('obj', (object,), {'percent': 60})()
        result = task_func()
        assert 'Memory Usage (%)' in result
        assert '60' in result

def test_task_func_disk_usage():
    with patch('psutil.disk_usage') as mock_disk_usage:
        mock_disk_usage.return_value = type('obj', (object,), {'percent': 70})()
        result = task_func()
        assert 'Disk Usage (%)' in result
        assert '70' in result

def test_task_func_table_format():
    result = task_func()
    assert isinstance(result, str)
    assert 'Item' in result
    assert 'Value' in result