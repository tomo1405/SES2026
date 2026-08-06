import pytest
from src_0460 import task_func

def test_task_func_with_valid_input():
    script_dir = "path/to/scripts"
    scripts = ["script1.py", "script2.py"]
    delay = 1
    start_times = task_func(script_dir, scripts, delay)
    assert len(start_times) == len(scripts)
    for start_time in start_times:
        assert start_time.strftime("%Y-%m-%d %H:%M:%S") == datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def test_task_func_with_invalid_input():
    script_dir = "path/to/scripts"
    scripts = []
    delay = 1
    with pytest.raises(ValueError):
        task_func(script_dir, scripts, delay)

    script_dir = "path/to/scripts"
    scripts = ["script1.py", "script2.py"]
    delay = -1
    with pytest.raises(ValueError):
        task_func(script_dir, scripts, delay)

def test_task_func_with_invalid_script():
    script_dir = "path/to/scripts"
    scripts = ["script1.py", "script2.py"]
    delay = 1
    with pytest.raises(FileNotFoundError):
        task_func(script_dir, scripts, delay)