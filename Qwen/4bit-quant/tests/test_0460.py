import pytest
from src_0460 import task_func

def test_task_func_valid_input():
    script_dir = "/path/to/scripts"
    scripts = ["script1.sh", "script2.sh"]
    delay = 1
    start_times = task_func(script_dir, scripts, delay)
    assert len(start_times) == 2
    assert all(isinstance(time_str, str) for time_str in start_times)

def test_task_func_no_scripts():
    script_dir = "/path/to/scripts"
    scripts = []
    delay = 1
    with pytest.raises(ValueError, match="No scripts provided."):
        task_func(script_dir, scripts, delay)

def test_task_func_negative_delay():
    script_dir = "/path/to/scripts"
    scripts = ["script1.sh"]
    delay = -1
    with pytest.raises(ValueError, match="delay cannot be negative."):
        task_func(script_dir, scripts, delay)

def test_task_func_script_not_found():
    script_dir = "/path/to/scripts"
    scripts = ["non_existent_script.sh"]
    delay = 1
    with pytest.raises(FileNotFoundError, match="Script not found: /path/to/scripts/non_existent_script.sh"):
        task_func(script_dir, scripts, delay)