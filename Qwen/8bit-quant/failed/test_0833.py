import pytest
from src_0833 import task_func
import os
import tempfile

def test_task_func_success():
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        filename = os.path.join(temp_dir, 'test_file.pkl')
        data = {'key': 'value'}

        # Call the function
        result = task_func(filename, data)

        # Assert that the function returned True
        assert result is True

        # Check if the file was created
        assert os.path.exists(filename)

        # Load the data from the file and check its contents
        with open(filename, 'rb') as f:
            loaded_data = pickle.load(f)
        assert loaded_data == data

def test_task_func_failure():
    # Create a read-only directory
    with tempfile.TemporaryDirectory() as temp_dir:
        os.chmod(temp_dir, 0o444)  # Make the directory read-only
        filename = os.path.join(temp_dir, 'test_file.pkl')
        data = {'key': 'value'}

        # Call the function
        result = task_func(filename, data)

        # Assert that the function returned False
        assert result is False

        # Check if the file was not created
        assert not os.path.exists(filename)

def test_task_func_nonexistent_directory():
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        filename = os.path.join(temp_dir, 'subdir', 'test_file.pkl')
        data = {'key': 'value'}

        # Call the function
        result = task_func(filename, data)

        # Assert that the function returned True
        assert result is True

        # Check if the subdirectory was created
        subdir = os.path.dirname(filename)
        assert os.path.exists(subdir)

        # Check if the file was created
        assert os.path.exists(filename)

        # Load the data from the file and check its contents
        with open(filename, 'rb') as f:
            loaded_data = pickle.load(f)
        assert loaded_data == data