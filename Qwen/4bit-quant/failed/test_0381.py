import pytest
from src_0381 import task_func
import os
import tempfile
import shutil

def create_temp_files(temp_dir, files):
    for file in files:
        with open(os.path.join(temp_dir, file), 'w') as f:
            f.write('Sample content')

def test_task_func():
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create some sample files
        files = ['file1.txt', 'file2.docx', 'file3.pdf', 'file4.txt']
        create_temp_files(temp_dir, files)

        # Run the task function
        task_func(temp_dir)

        # Check if directories for extensions exist and files are moved
        assert os.path.exists(os.path.join(temp_dir, 'txt'))
        assert os.path.exists(os.path.join(temp_dir, 'docx'))
        assert os.path.exists(os.path.join(temp_dir, 'pdf'))

        assert os.path.isfile(os.path.join(temp_dir, 'txt', 'file1.txt'))
        assert os.path.isfile(os.path.join(temp_dir, 'txt', 'file4.txt'))
        assert os.path.isfile(os.path.join(temp_dir, 'docx', 'file2.docx'))
        assert os.path.isfile(os.path.join(temp_dir, 'pdf', 'file3.pdf'))

def test_task_func_no_files():
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # Run the task function with no files
        task_func(temp_dir)

        # Check if any directories are created
        assert not os.listdir(temp_dir)

def test_task_func_no_extension():
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create a file with no extension
        with open(os.path.join(temp_dir, 'file'), 'w') as f:
            f.write('Sample content')

        # Run the task function
        task_func(temp_dir)

        # Check if no directories are created and file remains in place
        assert not os.listdir(temp_dir)