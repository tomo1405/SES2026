import pytest
from src_0717 import task_func
import os
import json
from datetime import datetime

@pytest.fixture
def temp_json_file(tmp_path):
    """Create a temporary JSON file for testing."""
    json_content = '{"key": "value"}'
    json_file = tmp_path / "test_json_file.json"
    with open(json_file, 'w') as f:
        f.write(json_content)
    return json_file

def test_task_func_updates_json(temp_json_file):
    # Call the function with the temporary JSON file
    result = task_func(json_file=str(temp_json_file))
    
    # Check if the file was updated correctly
    with open(temp_json_file, 'r') as f:
        updated_json = json.load(f)
    
    # Verify that 'last_updated' key is added and has a datetime value
    assert 'last_updated' in updated_json
    last_updated = datetime.fromisoformat(updated_json['last_updated'])
    assert isinstance(last_updated, datetime)
    
    # Verify that other content remains unchanged
    assert updated_json['key'] == 'value'

def test_task_func_appends_path():
    original_sys_path = list(sys.path)
    task_func()
    assert len(sys.path) == len(original_sys_path) + 1
    assert sys.path[-1] == PATH_TO_APPEND
    # Clean up by removing the appended path
    sys.path.pop()