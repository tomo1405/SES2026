import pytest
from unittest.mock import patch, MagicMock
from src_1029 import task_func

def test_task_func_invalid_interval():
    with pytest.raises(ValueError):
        task_func(-1, 10)

def test_task_func_invalid_duration():
    with pytest.raises(ValueError):
        task_func(1, -1)

def test_task_func_zero_interval():
    with pytest.raises(ValueError):
        task_func(0, 10)

def test_task_func_zero_duration():
    with pytest.raises(ValueError):
        task_func(10, 0)

@patch('src_1029.platform.system')
@patch('src_1029.subprocess.check_output')
@patch('src_1029.open', new_callable=MagicMock)
def test_task_func_windows(mock_open, mock_check_output, mock_platform_system):
    mock_platform_system.return_value = "Windows"
    mock_check_output.return_value = b'{"Time Stamp": "1633072800", "\\Processor(_Total)\\% Processor Time": "10.5"}'
    
    result = task_func(1, 2)
    assert result == "logfile.log"
    mock_open.assert_called_once_with("logfile.log", "w", encoding="utf-8")
    mock_check_output.assert_called_with([
        "typeperf",
        "\\Processor(_Total)\\% Processor Time",
        "-sc",
        "1",
    ])

@patch('src_1029.platform.system')
@patch('src_1029.subprocess.check_output')
@patch('src_1029.open', new_callable=MagicMock)
def test_task_func_unix(mock_open, mock_check_output, mock_platform_system):
    mock_platform_system.return_value = "Linux"
    mock_check_output.return_value = b'top - 16:00:00 up 1 day, 23:45,  1 user,  load average: 0.10, 0.05, 0.01\nTasks: 2 total, 1 running, 1 sleeping\n%Cpu(s): 10.5 us, 0.0 sy, 0.0 ni, 89.5 id, 0.0 wa, 0.0 hi, 0.0 si, 0.0 st\nKiB Mem :  8192000 total,  1234560 free,  2345678 used,  4608762 buff/cache\nKiB Swap:  4096000 total,  4096000 free,        0 used.  5678901 avail Mem '
    
    result = task_func(1, 2)
    assert result == "logfile.log"
    mock_open.assert_called_once_with("logfile.log", "w", encoding="utf-8")
    mock_check_output.assert_called_with(["top", "-b", "-n1"])

@patch('src_1029.time.sleep')
@patch('src_1029.platform.system')
@patch('src_1029.subprocess.check_output')
@patch('src_1029.open', new_callable=MagicMock)
def test_task_func_sleep_time(mock_open, mock_check_output, mock_platform_system, mock_sleep):
    mock_platform_system.return_value = "Windows"
    mock_check_output.return_value = b'{"Time Stamp": "1633072800", "\\Processor(_Total)\\% Processor Time": "10.5"}'
    
    task_func(2, 5)
    mock_sleep.assert_called_with(1)  # interval - operation time should be close to 1 second

@patch('src_1029.open', side_effect=IOError("Mocked IOError"))
def test_task_func_io_error(mock_open):
    result = task_func(1, 1)
    assert result is None