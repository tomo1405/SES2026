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
    test_dir = "test_directory"
    test_json_file = "test_file.json"
    test_data = {"key": "value"}
    
    # Test if directory exists
    with pytest.raises(FileNotFoundError):
        task_func("nonexistent_directory")
    
    # Test if JSON file is processed correctly
    os.makedirs(test_dir, exist_ok=True)
    with open(os.path.join(test_dir, test_json_file), "w") as file:
        json.dump(test_data, file)
    
    processed_files = task_func(test_dir)
    assert len(processed_files) == 1
    with open(processed_files[0], "r") as file:
        processed_data = json.load(file)
    assert processed_data == {"key": "value"}