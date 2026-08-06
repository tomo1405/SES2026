import pytest
from src_0378 import task_func
from unittest.mock import patch

def test_task_func_cpu_usage(mocker):
    mocker.patch('psutil.cpu_percent', return_value=50)
    result = task_func()
    assert 'CPU Usage (%): 50' in result

def test_task_func_memory_usage(mocker):
    mock_memory_info = mocker.Mock(percent=75)
    mocker.patch('psutil.virtual_memory', return_value=mock_memory_info)
    result = task_func()
    assert 'Memory Usage (%): 75' in result

def test_task_func_disk_usage(mocker):
    mock_disk_usage = mocker.Mock(percent=90)
    mocker.patch('psutil.disk_usage', return_value=mock_disk_usage)
    result = task_func()
    assert 'Disk Usage (%): 90' in result

def test_task_func_table_format(mocker):
    mocker.patch('psutil.cpu_percent', return_value=50)
    mocker.patch('psutil.virtual_memory', return_value=mocker.Mock(percent=75))
    mocker.patch('psutil.disk_usage', return_value=mocker.Mock(percent=90))
    result = task_func()
    assert 'Item' in result
    assert 'Value' in result
    assert 'CPU Usage (%)' in result
    assert 'Memory Usage (%)' in result
    assert 'Disk Usage (%)' in result