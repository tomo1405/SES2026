import pytest
from src_1104 import task_func
import os
import subprocess

@pytest.fixture
def setup():
    yield

def test_task_func_success(setup):
    script_path = "test_script.py"
    temp_dir = "/tmp"
    result = task_func(script_path=script_path, temp_dir=temp_dir)
    assert result == "Script executed successfully!"

def test_task_func_failure(setup):
    script_path = "nonexistent_script.py"
    temp_dir = "/tmp"
    result = task_func(script_path=script_path, temp_dir=temp_dir)
    assert result == "Script execution failed!"