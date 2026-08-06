import subprocess
import shutil
import os
import pytest

def task_func(script_path: str, temp_dir: str) -> str:
    try:
        shutil.copy(script_path, temp_dir)
        temp_script_path = os.path.join(temp_dir, os.path.basename(script_path))
        result = subprocess.call(["python", temp_script_path])
        print(result)
        if result == 0:
            return "Script executed successfully!"
        else:
            return "Script execution failed!"
    except Exception as e:
        return "Script execution failed!"

def test_task_func():
    script_path = "path/to/script.py"
    temp_dir = "path/to/temp/dir"
    result = task_func(script_path, temp_dir)
    assert result == "Script executed successfully!"

def test_task_func_exception():
    script_path = "path/to/script.py"
    temp_dir = "path/to/temp/dir"
    with pytest.raises(Exception):
        task_func(script_path, temp_dir)