import pytest
from src_0462 import task_func

def test_task_func_valid_script_path(tmp_path):
    script_path = tmp_path / "script.sh"
    script_path.write_text("echo 'Hello, world!'")
    result = task_func(str(script_path))
    assert result["CPU Usage"] > 0
    assert result["Memory Usage"] > 0

def test_task_func_invalid_script_path(tmp_path):
    script_path = tmp_path / "script.sh"
    script_path.write_text("echo 'Hello, world!'")
    result = task_func(str(script_path))
    assert result["CPU Usage"] == 0
    assert result["Memory Usage"] == 0

def test_task_func_timeout(tmp_path):
    script_path = tmp_path / "script.sh"
    script_path.write_text("while true; do :; done")
    result = task_func(str(script_path), timeout=0.1)
    assert result["CPU Usage"] == 0
    assert result["Memory Usage"] == 0