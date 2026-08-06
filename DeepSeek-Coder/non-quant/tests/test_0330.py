import pytest
from src_0330 import task_func
import os
import re
import json

@pytest.fixture
def sample_data():
    return {
        "file1.json": {
            "key1": "This is a test (sample) with (multiple) matches.",
            "key2": "Another (example) with matches."
        },
        "file2.json": {
            "key1": "Another (sample) with matches.",
            "key2": "Yet another (example) with matches."
        }
    }

@pytest.fixture
def sample_files(tmp_path):
    files = {}
    for filename, data in sample_data().items():
        file_path = tmp_path / filename
        with open(file_path, 'w') as file:
            json.dump(data, file)
        files[filename] = file_path
    return files

def test_task_func(sample_files, tmp_path):
    for filename, file_path in sample_files.items():
        result = task_func(file_path)
        assert isinstance(result, dict), "The function should return a dictionary."
        assert len(result) == 1, "The dictionary should contain one entry."
        assert list(result.keys())[0] == os.path.basename(file_path), "The key should be the filename."
        assert len(result[os.path.basename(file_path)]) > 0, "The list of matches should not be empty."