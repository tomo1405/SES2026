import pytest
from src_1104 import task_func

def test_task_func_valid_script():
    script_path = "path/to/valid/script.py"
    temp_dir = "path/to/temp/dir"
    result = task_func(script_path, temp_dir)
    assert result == "Script executed successfully!"

def test_task_func_invalid_script():
    script_path = "path/to/invalid/script.py"
    temp_dir = "path/to/temp/dir"
    result = task_func(script_path, temp_dir)
    assert result == "Script execution failed!"

def test_task_func_exception():
    script_path = "path/to/valid/script.py"
    temp_dir = "path/to/temp/dir"
    with pytest.raises(Exception):
        task_func(script_path, temp_dir)