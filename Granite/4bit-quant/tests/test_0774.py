import os
import re
import shutil
import pytest

SOURCE_DIR = '/source/dir'
TARGET_DIR = '/target/dir'
FILE_PATTERN = re.compile(r'^(.*?)-\d+\.json$')

def task_func():
    for filename in os.listdir(SOURCE_DIR):
        match = FILE_PATTERN.match(filename)
        if match is not None:
            prefix = match.group(1)
            new_filename = f'{prefix}.json'
            shutil.move(os.path.join(SOURCE_DIR, filename), os.path.join(TARGET_DIR, new_filename))

def test_task_func():
    # Create a temporary directory to use as the source directory
    source_dir = '/tmp/source_dir'
    os.makedirs(source_dir)
    
    # Create some test files in the source directory
    test_files = ['file-1.json', 'file-2.json', 'file-3.json']
    for filename in test_files:
        with open(os.path.join(source_dir, filename), 'w') as f:
            f.write('test file')
    
    # Call the function with the test source directory
    task_func()
    
    # Check that the files were moved to the target directory
    for filename in test_files:
        new_filename = filename.split('-')[0] + '.json'
        assert os.path.exists(os.path.join(TARGET_DIR, new_filename))
    
    # Clean up the temporary directory
    shutil.rmtree(source_dir)