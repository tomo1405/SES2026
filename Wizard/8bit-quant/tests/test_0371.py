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
    # Test case 1: directory exists
    directory_path = 'tests/test_data'
    assert task_func(directory_path) == ['tests/test_data/test1.json', 'tests/test_data/test2.json']
    
    # Test case 2: directory does not exist
    directory_path = 'tests/test_data_not_exist'
    with pytest.raises(FileNotFoundError):
        task_func(directory_path)