python
import os
import shutil
import glob
import pytest

def task_func(source_dir, dest_dir, extension):
    files = glob.glob(os.path.join(source_dir, f'*.{extension}'))
    
    for file in files:
        shutil.move(file, dest_dir)
        
    result = len(files)

    return result

def test_task_func():
    source_dir = 'source_dir'
    dest_dir = 'dest_dir'
    extension = 'txt'
    
    os.makedirs(source_dir, exist_ok=True)
    os.makedirs(dest_dir, exist_ok=True)
    
    with open(os.path.join(source_dir, 'file1.txt'), 'w') as f:
        f.write('test')
    with open(os.path.join(source_dir, 'file2.txt'), 'w') as f:
        f.write('test')
    with open(os.path.join(source_dir, 'file3.txt'), 'w') as f:
        f.write('test')
    
    assert task_func(source_dir, dest_dir, extension) == 3
    
    shutil.rmtree(source_dir)
    shutil.rmtree(dest_dir)