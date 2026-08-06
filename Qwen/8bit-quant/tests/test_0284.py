import pytest
from src_0284 import task_func
import os
import json
from collections import Counter

# Mocking os.listdir and os.path.join to control file listing and paths
class MockedListDir:
    def __init__(self, files):
        self.files = files

    def __call__(self, path):
        return self.files

class MockedPathJoin:
    def __init__(self, base_path):
        self.base_path = base_path

    def __call__(self, *args):
        return os.path.join(self.base_path, *args)

# Mocking json.load to control JSON file content
class MockedJsonLoad:
    def __init__(self, data_dict):
        self.data_dict = data_dict

    def __call__(self, file):
        return self.data_dict

@pytest.fixture
def setup_mocks(monkeypatch, tmpdir):
    # Create temporary directory and JSON files
    json_files = ['file1.json', 'file2.json', 'file3.json']
    for file in json_files:
        file_path = tmpdir.join(file)
        file_path.write_text(json.dumps({'name': 'Alice'}), 'utf-8')

    # Mock os.listdir and os.path.join
    monkeypatch.setattr(os, 'listdir', MockedListDir(json_files))
    monkeypatch.setattr(os.path, 'join', MockedPathJoin(str(tmpdir)))

    # Mock json.load
    monkeypatch.setattr(json, 'load', MockedJsonLoad({'name': 'Alice'}))

    return str(tmpdir)

def test_task_func(setup_mocks):
    result = task_func(json_files_path=setup_mocks, key='name')
    expected_result = {'Alice': 3}
    assert result == expected_result

def test_task_func_no_json_files(setup_mocks, monkeypatch):
    # Mock os.listdir to return no JSON files
    monkeypatch.setattr(os, 'listdir', MockedListDir([]))
    result = task_func(json_files_path=setup_mocks, key='name')
    expected_result = {}
    assert result == expected_result

def test_task_func_key_not_in_data(setup_mocks, monkeypatch):
    # Mock json.load to return data without the specified key
    monkeypatch.setattr(json, 'load', MockedJsonLoad({'age': 30}))
    result = task_func(json_files_path=setup_mocks, key='name')
    expected_result = {}
    assert result == expected_result