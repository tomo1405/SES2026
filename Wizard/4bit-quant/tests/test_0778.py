python
import os
import re
import zipfile
import pytest

from src_0778 import task_func

@pytest.fixture
def directory():
    return 'test_dir'

@pytest.fixture
def pattern():
    return r'^(.*?)-\d+\.zip$'

def test_task_func(directory, pattern):
    os.makedirs(directory, exist_ok=True)
    # Create a zip file with a name that matches the pattern
    with zipfile.ZipFile(os.path.join(directory, 'test-1.zip'), 'w') as zip_ref:
        zip_ref.writestr('test.txt', 'test')
    # Create another zip file with a different name that matches the pattern
    with zipfile.ZipFile(os.path.join(directory, 'test-2.zip'), 'w') as zip_ref:
        zip_ref.writestr('test.txt', 'test')
    # Call the task function with the directory and pattern
    extracted_dirs = task_func(directory, pattern)
    # Check that the function returns a list of two directories
    assert len(extracted_dirs) == 2
    # Check that the directories have been created
    assert os.path.exists(os.path.join(directory, 'test'))
    assert os.path.exists(os.path.join(directory, 'test-2'))
    # Check that the files have been extracted
    assert os.path.exists(os.path.join(directory, 'test', 'test.txt'))
    assert os.path.exists(os.path.join(directory, 'test-2', 'test.txt'))