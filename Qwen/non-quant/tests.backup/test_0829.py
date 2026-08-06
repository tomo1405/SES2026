import pytest
from src_0829 import task_func
import os
import tempfile

def test_task_func_success():
    # Create a temporary source file
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(b"Hello, world!")
        temp_file.close()

        # Create a temporary destination directory
        with tempfile.TemporaryDirectory() as temp_dir:
            # Call the function
            result = task_func(temp_file.name, temp_dir)

            # Check if the file was copied correctly
            assert os.path.exists(result)
            assert os.path.isfile(result)
            with open(result, 'rb') as f:
                assert f.read() == b"Hello, world!"

            # Check if the original file is empty
            with open(temp_file.name, 'rb') as f:
                assert f.read() == b""

            # Clean up
            os.remove(temp_file.name)

def test_task_func_nonexistent_file():
    with tempfile.TemporaryDirectory() as temp_dir:
        with pytest.raises(FileNotFoundError):
            task_func("nonexistent_file.txt", temp_dir)

def test_task_func_permission_error():
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.close()

        # Make the file read-only
        os.chmod(temp_file.name, 0o444)

        with tempfile.TemporaryDirectory() as temp_dir:
            with pytest.raises(PermissionError):
                task_func(temp_file.name, temp_dir)

        # Clean up
        os.chmod(temp_file.name, 0o666)
        os.remove(temp_file.name)

def test_task_func_existing_directory():
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(b"Hello, world!")
        temp_file.close()

        with tempfile.TemporaryDirectory() as temp_dir:
            # Create a subdirectory with the same name as the destination directory
            os.mkdir(os.path.join(temp_dir, "subdir"))

            # Call the function
            result = task_func(temp_file.name, os.path.join(temp_dir, "subdir"))

            # Check if the file was copied correctly
            assert os.path.exists(result)
            assert os.path.isfile(result)
            with open(result, 'rb') as f:
                assert f.read() == b"Hello, world!"

            # Check if the original file is empty
            with open(temp_file.name, 'rb') as f:
                assert f.read() == b""

            # Clean up
            os.remove(temp_file.name)