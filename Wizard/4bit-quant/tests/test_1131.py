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
    directory = 'empty_directory'
    os.mkdir(directory)
    assert task_func(directory) == str(Path(directory) / 'hashes.json')
    os.rmdir(directory)
    
    # Test case 3: directory contains files
    directory = 'directory_with_files'
    os.mkdir(directory)
    file1 = Path(directory) / 'file1.txt'
    file2 = Path(directory) / 'file2.txt'
    with open(file1, 'w') as f:
        f.write('Hello, world!')
    with open(file2, 'w') as f:
        f.write('Goodbye, world!')
    assert task_func(directory) == str(Path(directory) / 'hashes.json')
    os.remove(file1)
    os.remove(file2)
    os.rmdir(directory)
    
    # Test case 4: directory contains subdirectories
    directory = 'directory_with_subdirectories'
    os.mkdir(directory)
    subdir1 = Path(directory) / 'subdir1'
    subdir2 = Path(directory) / 'subdir2'
    os.mkdir(subdir1)
    os.mkdir(subdir2)
    file1 = Path(subdir1) / 'file1.txt'
    file2 = Path(subdir2) / 'file2.txt'
    with open(file1, 'w') as f:
        f.write('Hello, world!')
    with open(file2, 'w') as f:
        f.write('Goodbye, world!')
    assert task_func(directory) == str(Path(directory) / 'hashes.json')
    os.remove(file1)
    os.remove(file2)
    os.rmdir(subdir1)
    os.rmdir(subdir2)
    os.rmdir(directory)