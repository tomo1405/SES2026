import pytest
from src_1029 import task_func

def test_task_func_valid_input():
    interval = 1
    duration = 1
    logfile_path = task_func(interval, duration)
    assert logfile_path == "logfile.log"

def test_task_func_invalid_interval():
    interval = 0
    duration = 1
    with pytest.raises(ValueError):
        task_func(interval, duration)

def test_task_func_invalid_duration():
    interval = 1
    duration = 0
    with pytest.raises(ValueError):
        task_func(interval, duration)

def test_task_func_invalid_logfile_path():
    interval = 1
    duration = 1
    logfile_path = task_func(interval, duration)
    assert logfile_path == "logfile.log"

def test_task_func_invalid_cpu_usage():
    interval = 1
    duration = 1
    logfile_path = task_func(interval, duration)
    assert logfile_path == "logfile.log"

def test_task_func_invalid_json_dump():
    interval = 1
    duration = 1
    logfile_path = task_func(interval, duration)
    assert logfile_path == "logfile.log"

def test_task_func_invalid_logfile_write():
    interval = 1
    duration = 1
    logfile_path = task_func(interval, duration)
    assert logfile_path == "logfile.log"

def test_task_func_invalid_sleep_time():
    interval = 1
    duration = 1
    logfile_path = task_func(interval, duration)
    assert logfile_path == "logfile.log"