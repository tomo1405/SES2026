python
import os
import hashlib
import json
from pathlib import Path
import pytest

def task_func(directory: str) -> str:
    hash_dict = {}
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = Path(root) / file
            with open(file_path, 'rb') as f:
                bytes = f.read()  # read entire file as bytes
                readable_hash = hashlib.sha256(bytes).hexdigest()
                hash_dict[str(file_path)] = readable_hash
                
    # Save to JSON file
    json_file = Path(directory) / 'hashes.json'
    with open(json_file, 'w') as f:
        json.dump(hash_dict, f)
    return str(json_file)

def test_task_func():
    # Test case 1: directory does not exist
    with pytest.raises(FileNotFoundError):
        task_func('nonexistent_directory')
        
    # Test case 2: directory is empty
    with pytest.raises(ValueError):
        task_func('empty_directory')
        
    # Test case 3: directory contains a file
    with pytest.raises(ValueError):
        task_func('directory_with_file')
        
    # Test case 4: directory contains multiple files
    directory = 'directory_with_files'
    os.makedirs(directory)
    file1 = directory + '/file1.txt'
    file2 = directory + '/file2.txt'
    with open(file1, 'w') as f:
        f.write('Hello, world!')
    with open(file2, 'w') as f:
        f.write('Goodbye, world!')
    result = task_func(directory)
    assert os.path.isfile(result)
    assert os.path.getsize(result) > 0
    os.remove(result)
    os.rmdir(directory)