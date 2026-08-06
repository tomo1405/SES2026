import pytest
from src_1102 import task_func
import os
import glob
import tempfile
import subprocess

def create_test_script(file_path, content):
    with open(file_path, 'w') as f:
        f.write(content)

def test_task_func_with_no_scripts():
    with tempfile.TemporaryDirectory() as temp_dir:
        result = task_func(temp_dir)
        assert result == {}

def test_task_func_with_one_script():
    with tempfile.TemporaryDirectory() as temp_dir:
        script_path = os.path.join(temp_dir, 'test_script.py')
        create_test_script(script_path, 'print("Hello, World!")')
        result = task_func(temp_dir)
        assert len(result) == 1
        assert 'test_script.py' in result
        assert result['test_script.py'] > 0

def test_task_func_with_multiple_scripts():
    with tempfile.TemporaryDirectory() as temp_dir:
        script1_path = os.path.join(temp_dir, 'script1.py')
        script2_path = os.path.join(temp_dir, 'script2.py')
        create_test_script(script1_path, 'print("Script 1")')
        create_test_script(script2_path, 'print("Script 2")')
        result = task_func(temp_dir)
        assert len(result) == 2
        assert 'script1.py' in result
        assert 'script2.py' in result
        assert result['script1.py'] > 0
        assert result['script2.py'] > 0

def test_task_func_with_non_executable_script():
    with tempfile.TemporaryDirectory() as temp_dir:
        script_path = os.path.join(temp_dir, 'non_executable.py')
        create_test_script(script_path, 'print("This will not execute")')
        # Make the script non-executable
        os.chmod(script_path, 0o444)
        result = task_func(temp_dir)
        assert result == {}

def test_task_func_with_invalid_python_script():
    with tempfile.TemporaryDirectory() as temp_dir:
        script_path = os.path.join(temp_dir, 'invalid_script.py')
        create_test_script(script_path, 'invalid syntax')
        result = task_func(temp_dir)
        assert len(result) == 1
        assert 'invalid_script.py' in result
        assert result['invalid_script.py'] > 0