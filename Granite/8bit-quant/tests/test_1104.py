import subprocess
import shutil
import os
import pytest
from src_1104 import task_func

def test_task_func_success():
    script_path = "path/to/script.py"
    temp_dir = "path/to/temp/dir"
    with pytest.raises(subprocess.CalledProcessError) as excinfo:
        task_func(script_path, temp_dir)
    assert "Script executed successfully!" in str(excinfo.value)

def test_task_func_failure():
    script_path = "path/to/script.py"
    temp_dir = "path/to/temp/dir"
    with pytest.raises(subprocess.CalledProcessError) as excinfo:
        task_func(script_path, temp_dir)
    assert "Script execution failed!" in str(excinfo.value)

def test_task_func_exception():
    script_path = "path/to/script.py"
    temp_dir = "path/to/temp/dir"
    with pytest.raises(Exception) as excinfo:
        task_func(script_path, temp_dir)
    assert "Script execution failed!" in str(excinfo.value)