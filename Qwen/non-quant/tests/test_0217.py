import pytest
from src_0217 import task_func
import os
import json
from collections import Counter

# Mocking utilities
class MockOpen:
    def __init__(self, content):
        self.content = content

    def read(self):
        return self.content

class MockOsListdir:
    def __init__(self, files):
        self.files = files

    def listdir(self, path):
        return self.files

# Fixtures
@pytest.fixture
def mock_os(monkeypatch):
    def mock_listdir(path):
        return ['file1.json', 'file2.json']
    monkeypatch.setattr(os, 'listdir', mock_listdir)

@pytest.fixture
def mock_json(monkeypatch):
    def mock_load(file_obj):
        return {'text': 'hello world hello'}
    monkeypatch.setattr(json, 'load', mock_load)

@pytest.fixture
def mock_open(monkeypatch):
    def mock_open_func(filename, mode):
        return MockOpen('{"text": "hello world hello"}')
    monkeypatch.setattr('builtins.open', mock_open_func)

# Tests
def test_task_func(mock_os, mock_json, mock_open):
    json_dir_path = '/path/to/json/dir'
    word_count = 2
    result = task_func(json_dir_path, word_count)
    expected_result = [('hello', 2), ('world', 1)]
    assert result == expected_result

def test_task_func_no_json_files(mock_os, mock_json, mock_open, monkeypatch):
    def mock_listdir(path):
        return ['file1.txt', 'file2.json']
    monkeypatch.setattr(os, 'listdir', mock_listdir)
    json_dir_path = '/path/to/json/dir'
    word_count = 2
    result = task_func(json_dir_path, word_count)
    expected_result = [('hello', 2)]
    assert result == expected_result

def test_task_func_empty_text(mock_os, mock_json, mock_open, monkeypatch):
    def mock_load(file_obj):
        return {'text': ''}
    monkeypatch.setattr(json, 'load', mock_load)
    json_dir_path = '/path/to/json/dir'
    word_count = 2
    result = task_func(json_dir_path, word_count)
    expected_result = []
    assert result == expected_result

def test_task_func_no_files(mock_os, mock_json, mock_open, monkeypatch):
    def mock_listdir(path):
        return []
    monkeypatch.setattr(os, 'listdir', mock_listdir)
    json_dir_path = '/path/to/json/dir'
    word_count = 2
    result = task_func(json_dir_path, word_count)
    expected_result = []
    assert result == expected_result