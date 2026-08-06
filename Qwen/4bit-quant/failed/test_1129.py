import pytest
from src_1129 import task_func
import os
import json
import hashlib
import base64
import time

# Mocking the file system operations and time for consistent test results
class MockOpen:
    def __init__(self, content):
        self.content = content

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def read(self):
        return self.content

class MockTime:
    def __init__(self, fixed_time):
        self.fixed_time = fixed_time

    def time(self):
        return self.fixed_time

def test_task_func(mocker, tmpdir):
    # Prepare test data
    test_data = {
        "A": {
            "test_key": {
                "maindata": [
                    {"Info": "test_info"}
                ]
            }
        }
    }
    test_json_content = json.dumps(test_data)
    test_file_path = str(tmpdir / "test_file.json")

    # Write test data to a temporary file
    with open(test_file_path, 'w') as f:
        f.write(test_json_content)

    # Mock file opening and time
    mocker.patch('builtins.open', return_value=MockOpen(test_json_content))
    fixed_time = 1633072800  # Fixed timestamp for consistent filename
    mocker.patch('time.time', return_value=fixed_time)

    # Call the function
    result = task_func(test_file_path, "test_key")

    # Expected output
    expected_hashed_value = hashlib.sha256("test_info".encode()).digest()
    expected_hashed_str = base64.b64encode(expected_hashed_value).decode()
    expected_new_file_name = f"test_key_hashed_{fixed_time}.txt"
    expected_new_file_path = os.path.join(str(tmpdir), expected_new_file_name)

    # Check if the new file was created correctly
    assert os.path.exists(result)
    assert result == expected_new_file_path

    # Read the content of the new file
    with open(result, 'r') as f:
        actual_content = f.read()

    # Verify the content of the new file
    assert actual_content == expected_hashed_str

    # Clean up the temporary file
    os.remove(test_file_path)
    os.remove(result)