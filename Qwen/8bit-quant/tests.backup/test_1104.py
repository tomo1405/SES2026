import pytest
from src_1104 import task_func
import os
import tempfile

def test_task_func_success():
    with tempfile.TemporaryDirectory() as temp_dir:
        script_path = os.path.join(os.path.dirname(__file__), "test_script_success.py")
        with open(script_path, "w") as f:
            f.write("print('Hello, World!')")
        
        result = task_func(script_path, temp_dir)
        assert result == "Script executed successfully!"

def test_task_func_failure():
    with tempfile.TemporaryDirectory() as temp_dir:
        script_path = os.path.join(os.path.dirname(__file__), "test_script_failure.py")
        with open(script_path, "w") as f:
            f.write("import sys; sys.exit(1)")
        
        result = task_func(script_path, temp_dir)
        assert result == "Script execution failed!"

def test_task_func_nonexistent_file():
    with tempfile.TemporaryDirectory() as temp_dir:
        script_path = "nonexistent_script.py"
        result = task_func(script_path, temp_dir)
        assert result == "Script execution failed!"

def test_task_func_permission_error():
    with tempfile.TemporaryDirectory() as temp_dir:
        script_path = os.path.join(os.path.dirname(__file__), "test_script_permission_error.py")
        with open(script_path, "w") as f:
            f.write("print('Hello, World!')")
        
        # Change permissions to make the file non-executable
        os.chmod(script_path, 0o444)
        
        result = task_func(script_path, temp_dir)
        assert result == "Script execution failed!"