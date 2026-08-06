import pytest
from src_0460 import task_func

def test_task_func_delay_negative():
    with pytest.raises(ValueError):
        task_func("", [], -1)

def test_task_func_no_scripts():
    with pytest.raises(ValueError):
        task_func("", [], 0)

def test_task_func_script_not_found():
    with pytest.raises(FileNotFoundError):
        task_func("", ["script.py"], 0)

def test_task_func_success():
    start_times = task_func("", ["script.py"], 0)
    assert len(start_times) == 1
    assert start_times[0] == datetime.now().strftime("%Y-%m-%d %H:%M:%S")