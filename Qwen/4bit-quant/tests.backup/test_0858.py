import pytest
from src_0858 import task_func
import os
import tempfile

def test_task_func():
    # Create temporary directories and files for testing
    with tempfile.TemporaryDirectory() as source_dir, tempfile.TemporaryDirectory() as dest_dir:
        # Create some test files in the source directory
        test_files = [
            os.path.join(source_dir, 'file1.txt'),
            os.path.join(source_dir, 'file2.jpg'),
            os.path.join(source_dir, 'file3.docx'),
            os.path.join(source_dir, 'file4.pdf')
        ]
        for file in test_files:
            open(file, 'a').close()

        # Define the extensions to be moved
        extensions = ['.txt', '.jpg']

        # Call the function
        result = task_func(source_dir, dest_dir, extensions)

        # Check if the correct files were moved
        assert set(result) == {'file1.txt', 'file2.jpg'}

        # Check if the files are no longer in the source directory
        for file in test_files[:2]:
            assert not os.path.exists(file)

        # Check if the files are now in the destination directory
        for file in result:
            assert os.path.exists(os.path.join(dest_dir, file))

        # Check if the other files remain in the source directory
        for file in test_files[2:]:
            assert os.path.exists(file)

def test_task_func_no_matching_files():
    with tempfile.TemporaryDirectory() as source_dir, tempfile.TemporaryDirectory() as dest_dir:
        # Create some test files in the source directory
        test_files = [
            os.path.join(source_dir, 'file1.docx'),
            os.path.join(source_dir, 'file2.pdf')
        ]
        for file in test_files:
            open(file, 'a').close()

        # Define the extensions to be moved (none of which match the files in the source directory)
        extensions = ['.txt', '.jpg']

        # Call the function
        result = task_func(source_dir, dest_dir, extensions)

        # Check if no files were moved
        assert result == []

        # Check if the files are still in the source directory
        for file in test_files:
            assert os.path.exists(file)

def test_task_func_empty_source_directory():
    with tempfile.TemporaryDirectory() as source_dir, tempfile.TemporaryDirectory() as dest_dir:
        # Define the extensions to be moved
        extensions = ['.txt', '.jpg']

        # Call the function
        result = task_func(source_dir, dest_dir, extensions)

        # Check if no files were moved
        assert result == []

        # Check if the destination directory is still empty
        assert not os.listdir(dest_dir)

def test_task_func_nonexistent_source_directory():
    with tempfile.TemporaryDirectory() as dest_dir:
        # Define the extensions to be moved
        extensions = ['.txt', '.jpg']

        # Call the function with a non-existent source directory
        result = task_func('/nonexistent/source', dest_dir, extensions)

        # Check if no files were moved
        assert result == []

        # Check if the destination directory is still empty
        assert not os.listdir(dest_dir)