import json
import sys
from datetime import datetime

import pytest
from src_0717 import task_func


# Mocking sys.path and datetime to avoid side effects
class MockSysPath:
    def __init__(self):
        self.original_path = list(sys.path)

    def __enter__(self):
        sys.path = []

    def __exit__(self, exc_type, exc_value, traceback):
        sys.path = self.original_path

class MockDatetime:
    def __init__(self, fixed_datetime):
        self.fixed_datetime = fixed_datetime

    def now(self):
        return self.fixed_datetime

@pytest.fixture
def mock_sys_path():
    return MockSysPath()

@pytest.fixture
def mock_datetime():
    fixed_datetime = datetime(2023, 10, 1, 12, 0, 0)
    return MockDatetime(fixed_datetime)

@pytest.fixture
def json_file(tmpdir):
    json_content = '{"key": "value"}'
    json_file = tmpdir.join("json_file.json")
    json_file.write(json_content)
    return json_file.strpath

def test_task_func(mock_sys_path, mock_datetime, json_file):
    # Patching datetime.now to return a fixed value
    original_datetime_now = datetime.now
    datetime.now = mock_datetime.now

    # Calling the function with the temporary JSON file
    result = task_func(json_file=json_file)

    # Restoring the original datetime.now
    datetime.now = original_datetime_now

    # Asserting that the JSON file was updated correctly
    with open(json_file, 'r') as file:
        updated_json_data = json.load(file)

    assert updated_json_data == {
        'key': 'value',
        'last_updated': '2023-10-01 12:00:00'
    }

    # Asserting that sys.path was modified
    assert mock_sys_path.original_path != sys.path
    assert sys.path == [mock_sys_path.original_path[0], '/path/to/whatever']