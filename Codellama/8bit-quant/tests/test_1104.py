import pytest
from src_1104 import task_func

def test_task_func_success():
    script_path = "path/to/script.py"
    temp_dir = "path/to/temp/dir"
    result = task_func(script_path, temp_dir)
    assert result == "Script executed successfully!"

def test_task_func_failure():
    script_path = "path/to/script.py"
    temp_dir = "path/to/temp/dir"
    result = task_func(script_path, temp_dir)
    assert result == "Script execution failed!"