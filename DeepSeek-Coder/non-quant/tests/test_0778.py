import pytest
from src_0778 import task_func
import os
import zipfile
import re

@pytest.fixture
def setup():
    # Create a temporary directory for testing
    test_dir = os.path.join(os.getcwd(), 'test_dir')
    os.makedirs(test_dir, exist_ok=True)
    yield test_dir
    # Clean up: remove the test directory and its contents
    for root, dirs, files in os.walk(test_dir, topdown=False):
        for file in files:
            os.remove(os.path.join(root, file))
        for dir_name in dirs:
            os.rmdir(os.path.join(root, dir_name))
    os.rmdir(test_dir)

def test_task_func(setup):
    # Create a sample zip file
    zip_content = b'test content'
    zip_path = os.path.join(setup, 'test.zip')
    with open(zip_path, 'wb') as f:
        f.write(zip_content)
    
    # Call the function with the test directory
    result = task_func(setup)
    
    # Add assertions to verify the output
    assert len(result) == 1
    assert os.path.isdir(os.path.join(setup, 'test'))