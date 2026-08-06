import pytest
from src_0744 import task_func
import os
import json

@pytest.fixture
def setup():
    # Create a temporary directory and populate it with sample JSON files
    temp_dir = 'test_dir'
    os.makedirs(temp_dir, exist_ok=True)
    # Create sample JSON files
    with open(os.path.join(temp_dir, 'file1.json'), 'w') as f:
        json.dump({'is_key': 1, 'has_key': 2, 'can_key': 3, 'should_key': 4})
    with open(os.path.join(temp_dir, 'file2.json'), 'w') as f:
        json.dump({'is_key': 5, 'has_key': 6, 'can_key': 7, 'should_key': 8})
    yield temp_dir
    # Clean up
    for root, dirs, files in os.walk(temp_dir):
        for file in files:
            os.remove(os.path.join(root, file))
    os.rmdir(temp_dir)

def test_task_func(setup):
    result = task_func(setup)
    assert result == {'is_': 2, 'has_': 2, 'can_': 2, 'should_': 2}