python
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
    # Test case 1: source directory does not exist
    with pytest.raises(FileNotFoundError):
        task_func('nonexistent_dir', 'target_dir')
    
    # Test case 2: target directory does not exist
    source_dir = 'source_dir'
    target_dir = 'nonexistent_target_dir'
    os.makedirs(source_dir)
    new_files = task_func(source_dir, target_dir)
    assert len(new_files) == 0
    
    # Test case 3: target directory exists
    os.makedirs(target_dir)
    new_files = task_func(source_dir, target_dir)
    assert len(new_files) == 1
    
    # Test case 4: source directory contains multiple files
    os.remove(new_files[0])
    os.remove(os.path.join(source_dir, 'file1.txt'))
    os.remove(os.path.join(source_dir, 'file2.txt'))
    os.remove(os.path.join(source_dir, 'file3.txt'))
    os.makedirs(os.path.join(source_dir, 'subdir'))
    with open(os.path.join(source_dir, 'subdir', 'file4.txt'), 'w') as f:
        f.write('content')
    new_files = task_func(source_dir, target_dir)
    assert len(new_files) == 2
    
    # Test case 5: file content is hashed correctly
    with open(new_files[0], 'r') as f:
        content = f.read()
    assert content.startswith('#Hash: ')
    assert hashlib.md5(content[7:].encode()).hexdigest() == content.split('\n')[0][7:]
    
    # Test case 6: file content is unchanged
    with open(new_files[1], 'r') as f:
        content = f.read()
    assert content == 'content'