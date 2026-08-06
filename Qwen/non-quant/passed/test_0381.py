import pytest
from src_0381 import task_func
import os
import shutil
import tempfile

def test_task_func():
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create some files with different extensions
        file_paths = [
            os.path.join(temp_dir, 'file1.txt'),
            os.path.join(temp_dir, 'file2.docx'),
            os.path.join(temp_dir, 'file3.txt'),
            os.path.join(temp_dir, 'file4.pdf')
        ]
        for file_path in file_paths:
            with open(file_path, 'w') as f:
                f.write('Test content')

        # Run the function
        task_func(temp_dir)

        # Check if directories for each extension were created
        assert os.path.exists(os.path.join(temp_dir, 'txt'))
        assert os.path.exists(os.path.join(temp_dir, 'docx'))
        assert os.path.exists(os.path.join(temp_dir, 'pdf'))

        # Check if files were moved to the correct directories
        assert os.path.exists(os.path.join(temp_dir, 'txt', 'file1.txt'))
        assert os.path.exists(os.path.join(temp_dir, 'txt', 'file3.txt'))
        assert os.path.exists(os.path.join(temp_dir, 'docx', 'file2.docx'))
        assert os.path.exists(os.path.join(temp_dir, 'pdf', 'file4.pdf'))

        # Check if original files no longer exist
        for file_path in file_paths:
            assert not os.path.exists(file_path)

def test_task_func_no_files():
    # Create a temporary directory with no files
    with tempfile.TemporaryDirectory() as temp_dir:
        # Run the function
        task_func(temp_dir)

        # Check if any directories were created
        assert len(os.listdir(temp_dir)) == 0

def test_task_func_no_extensions():
    # Create a temporary directory with files that have no extensions
    with tempfile.TemporaryDirectory() as temp_dir:
        file_paths = [
            os.path.join(temp_dir, 'file1'),
            os.path.join(temp_dir, 'file2'),
            os.path.join(temp_dir, 'file3')
        ]
        for file_path in file_paths:
            with open(file_path, 'w') as f:
                f.write('Test content')

        # Run the function
        task_func(temp_dir)

        # Check if any directories were created
        assert len(os.listdir(temp_dir)) == 3  # Files should remain in place