import pytest
from src_1104 import task_func
import tempfile
import os

@pytest.fixture
def temp_directory():
    with tempfile.TemporaryDirectory() as temp_dir:
        yield temp_dir

@pytest.fixture
def script_file(tmp_path):
    script_content = """
print("Hello, World!")
"""
    script_path = tmp_path / "test_script.py"
    script_path.write_text(script_content)
    return script_path

def test_task_func_success(script_file, temp_directory):
    result = task_func(str(script_file), temp_directory)
    assert result == "Script executed successfully!"

def test_task_func_failure(temp_directory):
    non_existent_script_path = "/path/to/non_existent_script.py"
    result = task_func(non_existent_script_path, temp_directory)
    assert result == "Script execution failed!"

def test_task_func_exception(temp_directory):
    script_content = """
import sys
sys.exit(1)
"""
    script_path = temp_directory / "error_script.py"
    script_path.write_text(script_content)
    result = task_func(str(script_path), temp_directory)
    assert result == "Script execution failed!"