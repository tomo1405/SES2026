python
import os
import re
import json
import glob
import pytest

def task_func(directory_path: str) -> list:
    # Check if directory exists
    if not os.path.exists(directory_path):
        raise FileNotFoundError(f"Directory {directory_path} not found.")
    
    json_files = glob.glob(directory_path + '/*.json')
    processed_files = []
    
    for json_file in json_files:
        with open(json_file, 'r') as file:
            data = json.load(file)
        
        escaped_data = json.dumps(data, ensure_ascii=False)
        escaped_data = re.sub(r'(?<!\\)"', r'\\\"', escaped_data)
        
        with open(json_file, 'w') as file:
            file.write(escaped_data)
        
        processed_files.append(json_file)
    
    return processed_files

def test_task_func():
    # Test case 1: Directory does not exist
    with pytest.raises(FileNotFoundError):
        task_func('nonexistent_directory')
    
    # Test case 2: Directory exists, but no JSON files
    directory_path = 'tests/test_data/no_json_files'
    processed_files = task_func(directory_path)
    assert processed_files == []
    
    # Test case 3: Directory exists, JSON files exist
    directory_path = 'tests/test_data/json_files'
    processed_files = task_func(directory_path)
    assert processed_files == ['tests/test_data/json_files/test1.json', 'tests/test_data/json_files/test2.json']
    
    # Test case 4: Directory exists, JSON files exist, but some files are not valid JSON
    directory_path = 'tests/test_data/invalid_json_files'
    processed_files = task_func(directory_path)
    assert processed_files == ['tests/test_data/invalid_json_files/test1.json', 'tests/test_data/invalid_json_files/test2.json']
    
    # Test case 5: Directory exists, JSON files exist, but some files are not writable
    directory_path = 'tests/test_data/unwritable_files'
    processed_files = task_func(directory_path)
    assert processed_files == ['tests/test_data/unwritable_files/test1.json', 'tests/test_data/unwritable_files/test2.json']