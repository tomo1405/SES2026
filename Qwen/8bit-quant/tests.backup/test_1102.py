import pytest
from src_1102 import task_func
import os
import tempfile
import shutil

def create_temp_python_files(temp_dir, file_names):
    for file_name in file_names:
        with open(os.path.join(temp_dir, file_name), 'w') as f:
            f.write('print("Hello, World!")')

def test_task_func():
    # Create a temporary directory
    temp_dir = tempfile.mkdtemp()

    try:
        # Create some Python files in the temporary directory
        create_temp_python_files(temp_dir, ['script1.py', 'script2.py'])

        # Call the task_func
        result = task_func(temp_dir)

        # Check that the result is a dictionary
        assert isinstance(result, dict)

        # Check that each script's execution time is present and positive
        for file_name in ['script1.py', 'script2.py']:
            assert file_name in result
            assert result[file_name] > 0

    finally:
        # Clean up the temporary directory
        shutil.rmtree(temp_dir)