import pytest
from src_0462 import task_func

def test_task_func_valid_script_path():
    script_path = "path/to/script.sh"
    timeout = 10
    result = task_func(script_path, timeout)
    assert result["CPU Usage"] > 0
    assert result["Memory Usage"] > 0

def test_task_func_invalid_script_path():
    script_path = "path/to/invalid/script.sh"
    timeout = 10
    with pytest.raises(FileNotFoundError):
        task_func(script_path, timeout)

def test_task_func_timeout():
    script_path = "path/to/script.sh"
    timeout = 0.01
    result = task_func(script_path, timeout)
    assert result["CPU Usage"] == 0
    assert result["Memory Usage"] == 0