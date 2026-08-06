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
    new_files = task_func('source_dir', 'nonexistent_dir')
    assert len(new_files) == 0
    
    # Test case 3: target directory exists
    os.makedirs('target_dir')
    new_files = task_func('source_dir', 'target_dir')
    assert len(new_files) == 1
    
    # Test case 4: target directory exists and contains files
    os.makedirs('target_dir/subdir')
    with open('target_dir/file1.txt', 'w') as f:
        f.write('content1')
    with open('target_dir/file2.txt', 'w') as f:
        f.write('content2')
    new_files = task_func('source_dir', 'target_dir')
    assert len(new_files) == 3
    
    # Test case 5: target directory exists and contains files with same name
    os.makedirs('target_dir/subdir2')
    with open('target_dir/subdir2/file1.txt', 'w') as f:
        f.write('content1')
    with open('target_dir/subdir2/file2.txt', 'w') as f:
        f.write('content2')
    new_files = task_func('source_dir', 'target_dir')
    assert len(new_files) == 5
    
    # Test case 6: target directory exists and contains files with same name and prefix
    os.makedirs('target_dir/subdir3')
    with open('target_dir/subdir3/file1.txt', 'w') as f:
        f.write('content1')
    with open('target_dir/subdir3/file2.txt', 'w') as f:
        f.write('content2')
    new_files = task_func('source_dir', 'target_dir', prefix='//Hash: ')
    assert len(new_files) == 7