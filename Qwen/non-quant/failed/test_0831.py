import pytest
from src_0831 import task_func
import os
import json
import tempfile

def test_task_func_success():
    # Create a temporary file and data to write
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        filename = temp_file.name
        data = {"key": "value"}

        # Call the function
        result, written_data = task_func(filename, data)

        # Assertions
        assert result is True
        assert written_data == data

        # Clean up
        os.remove(filename)

def test_task_func_file_not_created():
    # Use a non-writable directory
    filename = "/nonexistent/directory/file.json"
    data = {"key": "value"}

    # Call the function
    result, written_data = task_func(filename, data)

    # Assertions
    assert result is False
    assert written_data is None

def test_task_func_content_mismatch():
    # Create a temporary file and data to write
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        filename = temp_file.name
        data = {"key": "value"}
        incorrect_data = {"wrong_key": "wrong_value"}

        # Write incorrect data to the file first
        with open(filename, 'w') as f:
            json.dump(incorrect_data, f)

        # Call the function
        result, written_data = task_func(filename, data)

        # Assertions
        assert result is False
        assert written_data is None

        # Clean up
        os.remove(filename)

def test_task_func_exception():
    # Mock os.path.exists to raise an exception
    def mock_exists(path):
        raise OSError("Mocked OS error")

    # Patch os.path.exists
    with pytest.raises(OSError), pytest.MonkeyPatch.context() as mp:
        mp.setattr(os.path, 'exists', mock_exists)
        filename = "test_file.json"
        data = {"key": "value"}

        # Call the function
        result, written_data = task_func(filename, data)

        # Assertions
        assert result is False
        assert written_data is None