import pytest
from src_0674 import task_func
import os
import shutil

def test_task_func(tmpdir):
    # Create a temporary directory for testing
    temp_dir = tmpdir.mkdir("test_directory")

    # Define the number of files to create
    n_files = 5

    # Call the function under test
    result = task_func(str(temp_dir), n_files)

    # Check if the function returns the correct number of files
    assert result == n_files

    # Check if the files are created in the directory
    created_files = [f for f in os.listdir(str(temp_dir)) if os.path.isfile(os.path.join(str(temp_dir), f))]
    assert len(created_files) == n_files

    # Check if each file contains a single digit
    for i in range(n_files):
        filename = os.path.join(str(temp_dir), f"file_{i+1}.txt")
        with open(filename, 'r') as file:
            content = file.read()
            assert len(content) == 1
            assert content.isdigit()

    # Clean up the temporary directory
    shutil.rmtree(str(temp_dir))