import os
import glob
import hashlib
import pytest

def task_func(source_dir, target_dir, prefix='#Hash: '):
    if not os.path.exists(source_dir):
        raise FileNotFoundError(f"Source directory '{source_dir}' does not exist.")
    
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    
    new_files = []
    for file_path in glob.glob(os.path.join(source_dir, '*')):
        with open(file_path, 'r') as infile:
            content = infile.read()
        
        hash_object = hashlib.md5(content.encode())
        new_file_path = os.path.join(target_dir, os.path.basename(file_path))
        
        with open(new_file_path, 'w') as outfile:
            outfile.write(f"{prefix}{hash_object.hexdigest()}\n{content}")
        
        new_files.append(new_file_path)
    
    return new_files

def test_task_func():
    source_dir = "test_data/source"
    target_dir = "test_data/target"
    prefix = "#Hash: "
    new_files = task_func(source_dir, target_dir, prefix)
    assert len(new_files) > 0
    for file_path in new_files:
        with open(file_path, 'r') as infile:
            content = infile.read()
        assert content.startswith(prefix)
        assert len(content.splitlines()) == 2

if __name__ == "__main__":
    pytest.main()