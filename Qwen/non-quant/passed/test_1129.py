import pytest
from src_1129 import task_func
import os
import json
import hashlib
import base64
import time

# Mocking the time module to control the timestamp in the filename
class MockTime:
    def __init__(self, fixed_time):
        self.fixed_time = fixed_time

    def time(self):
        return self.fixed_time

@pytest.fixture
def mock_time(monkeypatch):
    mock_time_instance = MockTime(1633072800)  # Example fixed time
    monkeypatch.setattr(time, 'time', mock_time_instance.time)
    return mock_time_instance

@pytest.fixture
def temp_file(tmpdir):
    file_content = {
        "A": {
            "test_key": {
                "maindata": [
                    {"Info": "example_info"}
                ]
            }
        }
    }
    temp_file_path = tmpdir.join("temp.json")
    with open(temp_file_path, 'w') as f:
        json.dump(file_content, f)
    return str(temp_file_path)

def test_task_func(temp_file, mock_time):
    unknown_key = "test_key"
    result_path = task_func(temp_file, unknown_key)
    expected_file_name = f"{unknown_key}_hashed_{int(mock_time.fixed_time)}.txt"
    expected_file_path = os.path.join(os.getcwd(), expected_file_name)

    assert result_path == expected_file_path
    assert os.path.exists(expected_file_path)

    with open(expected_file_path, 'r') as f:
        hashed_str = f.read()

    original_value = "example_info"
    hashed_value = hashlib.sha256(original_value.encode()).digest()
    expected_hashed_str = base64.b64encode(hashed_value).decode()

    assert hashed_str == expected_hashed_str