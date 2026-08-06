import pytest
from src_0811 import task_func
import os
import subprocess
import tempfile

def test_task_func_no_execute():
    # Create a temporary directory and some files
    with tempfile.TemporaryDirectory() as temp_dir:
        os.makedirs(os.path.join(temp_dir, 'subdir'))
        with open(os.path.join(temp_dir, 'file1.txt'), 'w') as f:
            f.write('content1')
        with open(os.path.join(temp_dir, 'subdir', 'file2.exe'), 'w') as f:
            f.write('content2')

        # Run the function without executing files
        results = task_func(temp_dir, r'\.exe$', execute_files=False)

        # Check that the results contain the correct file paths
        expected_results = [
            os.path.join(temp_dir, 'subdir', 'file2.exe')
        ]
        assert results == expected_results

def test_task_func_execute():
    # Create a temporary directory and a script file
    with tempfile.TemporaryDirectory() as temp_dir:
        with open(os.path.join(temp_dir, 'script.sh'), 'w') as f:
            f.write('#!/bin/bash\necho "Hello, World!"')
        os.chmod(os.path.join(temp_dir, 'script.sh'), 0o755)

        # Run the function with executing files
        results = task_func(temp_dir, r'\.sh$', execute_files=True)

        # Check that the results contain the correct output from the script
        expected_results = ['Hello, World!\n']
        assert results == expected_results

def test_task_func_no_matching_files():
    # Create a temporary directory with no matching files
    with tempfile.TemporaryDirectory() as temp_dir:
        with open(os.path.join(temp_dir, 'file1.txt'), 'w') as f:
            f.write('content1')

        # Run the function
        results = task_func(temp_dir, r'\.exe$')

        # Check that the results are empty
        assert results == []

def test_task_func_empty_directory():
    # Create an empty temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # Run the function
        results = task_func(temp_dir, r'\.exe$')

        # Check that the results are empty
        assert results == []