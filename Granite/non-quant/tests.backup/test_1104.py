import subprocess
import shutil
import os
import pytest
from src_1104 import task_func

def test_task_func_success(tmp_path):
    script_path = "path/to/script.py"
    temp_dir = str(tmp_path)
    with open(script_path, "w") as f:
        f.write("print('Hello, world!')")
    result = task_func(script_path, temp_dir)
    assert result == "Script executed successfully!"

def test_task_func_failure(tmp_path):
    script_path = "path/to/script.py"
    temp_dir = str(tmp_path)
    with open(script_path, "w") as f:
        f.write("print('Hello, world!')")
    result = task_func(script_path, temp_dir)
    assert result == "Script execution failed!"

def test_task_func_exception(tmp_path):
    script_path = "path/to/script.py"
    temp_dir = str(tmp_path)
    with open(script_path, "w") as f:
        f.write("print('Hello, world!')")
    result = task_func(script_path, temp_dir)
    assert result == "Script execution failed!"