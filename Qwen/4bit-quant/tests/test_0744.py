import json
import os

import pytest
from src_0744 import task_func


# Mocking os and json modules to avoid file system operations during testing
class MockedList(list):
    def __init__(self, items):
        self.items = items

    def append(self, item):
        self.items.append(item)

class MockOs:
    @staticmethod
    def listdir(path):
        return ['file1.json', 'file2.json']

class MockJson:
    @staticmethod
    def load(file):
        if file.name.endswith('file1.json'):
            return {'is_active': True, 'has_permission': False}
        elif file.name.endswith('file2.json'):
            return {'can_edit': True, 'should_save': True}

@pytest.fixture
def mock_os(monkeypatch):
    monkeypatch.setattr(os, 'listdir', MockOs.listdir)

@pytest.fixture
def mock_json(monkeypatch):
    monkeypatch.setattr(json, 'load', MockJson.load)

def test_task_func(mock_os, mock_json, tmp_path):
    # Create a temporary directory and add mock JSON files
    dir_path = tmp_path / 'test_dir'
    dir_path.mkdir()

    file1_path = dir_path / 'file1.json'
    with file1_path.open('w') as f:
        json.dump({'is_active': True, 'has_permission': False}, f)

    file2_path = dir_path / 'file2.json'
    with file2_path.open('w') as f:
        json.dump({'can_edit': True, 'should_save': True}, f)

    # Expected result based on the mock JSON files
    expected_result = {
        'is_': 1,
        'has_': 1,
        'can_': 1,
        'should_': 1
    }

    # Call the function and assert the result
    result = task_func(str(dir_path))
    assert result == expected_result