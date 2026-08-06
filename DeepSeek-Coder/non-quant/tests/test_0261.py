import pytest
from src_0261 import task_func
import os
import json
import glob

@pytest.fixture
def setup_and_teardown():
    # Create a temporary directory and files for testing
    os.makedirs('test_dir', exist_ok=True)
    with open('test_dir/test_file.json', 'w') as f:
        json.dump({'key': 'value'}, f)
    yield
    # Clean up
    os.remove('test_dir/test_file.json')
    os.rmdir('test_dir')

def test_task_func(setup_and_teardown):
    assert task_func('test_dir') == 1