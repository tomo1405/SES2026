import pytest
from src_0401 import task_func
import os
import json

# Helper function to create temporary JSON files for testing
def create_temp_json_files(directory, contents_list):
    os.makedirs(directory, exist_ok=True)
    for i, content in enumerate(contents_list):
        file_path = os.path.join(directory, f"file_{i}.json")
        with open(file_path, 'w') as f:
            json.dump(content, f)

# Helper function to remove temporary directory and its contents
def cleanup_temp_directory(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        os.remove(file_path)
    os.rmdir(directory)

@pytest.fixture
def temp_directory(tmpdir):
    return str(tmpdir)

def test_task_func_finds_matching_string(temp_directory):
    contents_list = [
        {"key": "value1"},
        {"key": "value2"},
        {"key": "value3"}
    ]
    create_temp_json_files(temp_directory, contents_list)
    
    result = task_func(temp_directory, "value2")
    assert len(result) == 1
    assert result[0].endswith("file_1.json")
    
    cleanup_temp_directory(temp_directory)

def test_task_func_no_matches(temp_directory):
    contents_list = [
        {"key": "value1"},
        {"key": "value2"},
        {"key": "value3"}
    ]
    create_temp_json_files(temp_directory, contents_list)
    
    result = task_func(temp_directory, "non_existent_value")
    assert len(result) == 0
    
    cleanup_temp_directory(temp_directory)

def test_task_func_empty_directory(temp_directory):
    result = task_func(temp_directory, "any_value")
    assert len(result) == 0

def test_task_func_non_json_file(temp_directory):
    os.makedirs(os.path.join(temp_directory, "subdir"), exist_ok=True)
    with open(os.path.join(temp_directory, "subdir", "non_json.txt"), 'w') as f:
        f.write("This is not a JSON file.")
    
    contents_list = [
        {"key": "value1"}
    ]
    create_temp_json_files(temp_directory, contents_list)
    
    result = task_func(temp_directory, "value1")
    assert len(result) == 1
    assert result[0].endswith("file_0.json")
    
    cleanup_temp_directory(temp_directory)

def test_task_func_invalid_json_file(temp_directory):
    os.makedirs(os.path.join(temp_directory, "subdir"), exist_ok=True)
    with open(os.path.join(temp_directory, "subdir", "invalid_json.json"), 'w') as f:
        f.write("Invalid JSON")
    
    contents_list = [
        {"key": "value1"}
    ]
    create_temp_json_files(temp_directory, contents_list)
    
    result = task_func(temp_directory, "value1")
    assert len(result) == 1
    assert result[0].endswith("file_0.json")
    
    cleanup_temp_directory(temp_directory)