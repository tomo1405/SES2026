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

        # Assert the results
        assert success is True
        assert result == data

        # Clean up the temporary file
        os.remove(filename)

def test_task_func_file_not_created():
    # Use a non-writable path to simulate file creation failure
    filename = "/nonexistent/path/file.json"
    data = {"key": "value"}

    # Call the function
    success, result = task_func(filename, data)

    # Assert the results
    assert success is False
    assert result is None

def test_task_func_content_mismatch():
    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        filename = temp_file.name
        data = {"key": "value"}
        wrong_data = {"wrong_key": "wrong_value"}

        # Write incorrect data to the file
        with open(filename, 'w') as f:
            json.dump(wrong_data, f)

        # Call the function
        success, result = task_func(filename, data)

        # Assert the results
        assert success is False
        assert result is None

        # Clean up the temporary file
        os.remove(filename)

def test_task_func_exception():
    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        filename = temp_file.name
        data = {"key": "value"}

        # Mock an exception during file operations
        def mock_dump(*args, **kwargs):
            raise Exception("Mocked exception")

        original_dump = json.dump
        json.dump = mock_dump

        try:
            # Call the function
            success, result = task_func(filename, data)

            # Assert the results
            assert success is False
            assert result is None
        finally:
            # Restore the original json.dump function
            json.dump = original_dump

        # Clean up the temporary file
        os.remove(filename)