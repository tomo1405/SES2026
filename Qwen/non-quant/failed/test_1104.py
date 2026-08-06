import pytest
from src_1104 import task_func
import os
import tempfile

def test_task_func_success():
    # Create a temporary directory and a sample script file
    with tempfile.TemporaryDirectory() as temp_dir:
        script_path = os.path.join(temp_dir, "sample_script.py")
        with open(script_path, "w") as f:
            f.write("print('Hello, World!')")
        
        # Call the function with the path to the script and the temporary directory
        result = task_func(script_path, temp_dir)
        
        # Assert that the function returns the expected success message
        assert result == "Script executed successfully!"

def test_task_func_failure():
    # Create a temporary directory and a sample script file that will fail
    with tempfile.TemporaryDirectory() as temp_dir:
        script_path = os.path.join(temp_dir, "failing_script.py")
        with open(script_path, "w") as f:
            f.write("import sys; sys.exit(1)")
        
        # Call the function with the path to the script and the temporary directory
        result = task_func(script_path, temp_dir)
        
        # Assert that the function returns the expected failure message
        assert result == "Script execution failed!"

def test_task_func_exception():
    # Create a temporary directory and a non-existent script path
    with tempfile.TemporaryDirectory() as temp_dir:
        script_path = os.path.join(temp_dir, "non_existent_script.py")
        
        # Call the function with a non-existent script path and the temporary directory
        result = task_func(script_path, temp_dir)
        
        # Assert that the function returns the expected failure message due to exception
        assert result == "Script execution failed!"