import pytest
from src_0401 import task_func
from glob import glob
import os
import tempfile
import json

@pytest.fixture
def create_temp_json_files(tmpdir):
    dir_path = str(tmpdir)
    files = [
        {"file_name": "file1.json", "content": '{"key": "value1"}'},
        {"file_name": "file2.json", "content": '{"key": "value2"}'},
        {"file_name": "file3.json", "content": '{"key": "value3"}'},
        {"file_name": "file4.txt", "content": "This is not a JSON file"}
    ]
    
    for file_info in files:
        file_path = os.path.join(dir_path, file_info["file_name"])
        with open(file_path, 'w') as f:
            if file_info["file_name"].endswith(".json"):
                json.dump(file_info["content"], f)
            else:
                f.write(file_info["content"])
    
    return dir_path

def test_task_func(create_temp_json_files):
    directory = create_temp_json_files
    string_to_search = "value2"
    expected_result = [os.path.join(directory, "file2.json")]
    
    result = task_func(directory, string_to_search)
    
    assert result == expected_result

def test_task_func_no_match(create_temp_json_files):
    directory = create_temp_json_files
    string_to_search = "non_existent_value"
    expected_result = []
    
    result = task_func(directory, string_to_search)
    
    assert result == expected_result

def test_task_func_invalid_json(create_temp_json_files):
    directory = create_temp_json_files
    # Create an invalid JSON file
    invalid_json_file_path = os.path.join(directory, "invalid.json")
    with open(invalid_json_file_path, 'w') as f:
        f.write("{invalid json}")
    
    string_to_search = "value1"
    expected_result = [os.path.join(directory, "file1.json")]
    
    result = task_func(directory, string_to_search)
    
    assert result == expected_result

def test_task_func_empty_directory(tmpdir):
    directory = str(tmpdir)
    string_to_search = "value1"
    expected_result = []
    
    result = task_func(directory, string_to_search)
    
    assert result == expected_result