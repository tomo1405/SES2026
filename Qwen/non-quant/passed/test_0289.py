import pytest
from src_0289 import task_func
import os
import json

def test_task_func_no_json_files(tmpdir):
    # Create a temporary directory with no JSON files
    temp_dir = tmpdir.mkdir("test_dir")
    
    # Call the function
    result = task_func(str(temp_dir))
    
    # Assert that the result is an empty dictionary
    assert result == {}

def test_task_func_single_json_file(tmpdir):
    # Create a temporary directory with a single JSON file
    temp_dir = tmpdir.mkdir("test_dir")
    json_file = temp_dir.join("test.json")
    json_file.write(json.dumps({"key1": "value1", "key2": "value2"}))
    
    # Call the function
    result = task_func(str(temp_dir))
    
    # Assert that the result contains the correct key counts
    assert result == {"key1": 1, "key2": 1}

def test_task_func_multiple_json_files(tmpdir):
    # Create a temporary directory with multiple JSON files
    temp_dir = tmpdir.mkdir("test_dir")
    json_file1 = temp_dir.join("test1.json")
    json_file1.write(json.dumps({"key1": "value1", "key2": "value2"}))
    json_file2 = temp_dir.join("test2.json")
    json_file2.write(json.dumps({"key2": "value3", "key3": "value4"}))
    
    # Call the function
    result = task_func(str(temp_dir))
    
    # Assert that the result contains the correct key counts
    assert result == {"key1": 1, "key2": 2, "key3": 1}

def test_task_func_non_json_files(tmpdir):
    # Create a temporary directory with non-JSON files
    temp_dir = tmpdir.mkdir("test_dir")
    txt_file = temp_dir.join("test.txt")
    txt_file.write("This is a text file.")
    
    # Call the function
    result = task_func(str(temp_dir))
    
    # Assert that the result is an empty dictionary
    assert result == {}

def test_task_func_empty_json_files(tmpdir):
    # Create a temporary directory with empty JSON files
    temp_dir = tmpdir.mkdir("test_dir")
    json_file1 = temp_dir.join("test1.json")
    json_file1.write(json.dumps({}))
    json_file2 = temp_dir.join("test2.json")
    json_file2.write(json.dumps({}))
    
    # Call the function
    result = task_func(str(temp_dir))
    
    # Assert that the result is an empty dictionary
    assert result == {}