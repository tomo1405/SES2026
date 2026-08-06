import os
import re
import shutil
import tempfile

import pytest
from src_0774 import task_func

# Mocking constants
SOURCE_DIR = '/source/dir'
TARGET_DIR = '/target/dir'
FILE_PATTERN = re.compile(r'^(.*?)-\d+\.json$')

@pytest.fixture
def setup_directories():
    # Create temporary directories for source and target
    temp_source_dir = tempfile.mkdtemp()
    temp_target_dir = tempfile.mkdtemp()
    
    # Create files in the source directory
    for i in range(3):
        with open(os.path.join(temp_source_dir, f'file-{i}.json'), 'w') as f:
            f.write(f'Content of file-{i}.json')
    
    yield temp_source_dir, temp_target_dir
    
    # Clean up temporary directories
    shutil.rmtree(temp_source_dir)
    shutil.rmtree(temp_target_dir)

def test_task_func(setup_directories):
    source_dir, target_dir = setup_directories
    
    # Set global constants to use the temporary directories
    global SOURCE_DIR, TARGET_DIR
    SOURCE_DIR = source_dir
    TARGET_DIR = target_dir
    
    # Run the function
    task_func()
    
    # Check if files have been moved correctly
    assert not os.listdir(SOURCE_DIR)  # Source directory should be empty
    assert len(os.listdir(TARGET_DIR)) == 3  # Target directory should have 3 files
    
    for i in range(3):
        assert os.path.exists(os.path.join(TARGET_DIR, f'file.json'))  # All files should be renamed to 'file.json'

# Run the tests
if __name__ == '__main__':
    pytest.main()