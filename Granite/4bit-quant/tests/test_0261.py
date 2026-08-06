import json
import os
import glob
from src_0261 import task_func
import pytest

# Constants
KEY = 'mynewkey'
VALUE = 'mynewvalue'

def test_task_func():
    directory = '/path/to/directory'
    updated_files = task_func(directory)
    assert updated_files >= 0, "The function should return a non-negative integer"

    for file in glob.glob(os.path.join(directory, '*.json')):
        with open(file, 'r') as f:
            data = json.load(f)
            assert KEY in data, "The updated file should contain the new key"
            assert data[KEY] == VALUE, "The value of the new key should be the new value"