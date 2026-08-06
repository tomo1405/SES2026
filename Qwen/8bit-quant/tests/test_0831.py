import json
import os
import tempfile

from src_0831 import task_func


def test_task_func_success():
    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        filename = temp_file.name
        data = {"key": "value"}

        # Call the function
        success, result = task_func(filename, data)

        # Check if the function returns True and the correct data
        assert success is True
        assert result == data

        # Check if the file exists and contains the correct data
        assert os.path.exists(filename)
        with open(filename, 'r') as f:
            written_data = json.load(f)
            assert written_data == data

    # Clean up the temporary file
    os.remove(filename)

def test_task_func_file_not_found():
    # Use a non-existent filename
    filename = "non_existent_file.json"
    data = {"key": "value"}

    # Call the function
    success, result = task_func(filename, data)

    # Check if the function returns False and None
    assert success is False
    assert result is None

def test_task_func_read_write_mismatch():
    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        filename = temp_file.name
        data = {"key": "value"}

        # Write some different data to the file manually
        with open(filename, 'w') as f:
            f.write('{"different_key": "different_value"}')

        # Call the function
        success, result = task_func(filename, data)

        # Check if the function returns False and None
        assert success is False
        assert result is None

    # Clean up the temporary file
    os.remove(filename)

def test_task_func_exception_handling():
    # Create a temporary file that cannot be written to
    filename = "/non_writable_file.json"
    data = {"key": "value"}

    # Call the function
    success, result = task_func(filename, data)

    # Check if the function returns False and None
    assert success is False
    assert result is None