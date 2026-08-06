import pytest
from src_0284 import task_func
import os
import json
from collections import Counter

# Mocking os.listdir and json.load to simulate file operations
class MockedListDir:
    def __init__(self, files):
        self.files = files

    def __call__(self, path):
        return self.files

class MockedJsonLoad:
    def __init__(self, data):
        self.data = data

    def __call__(self, file):
        return self.data

def test_task_func_no_json_files(monkeypatch):
    monkeypatch.setattr(os, 'listdir', MockedListDir([]))
    result = task_func()
    assert result == {}

def test_task_func_one_json_file_with_key(monkeypatch):
    json_data = {'name': 'Alice'}
    monkeypatch.setattr(os, 'listdir', MockedListDir(['file1.json']))
    monkeypatch.setattr(json, 'load', MockedJsonLoad(json_data))
    result = task_func()
    assert result == {'Alice': 1}

def test_task_func_multiple_json_files_with_same_key(monkeypatch):
    json_data1 = {'name': 'Alice'}
    json_data2 = {'name': 'Bob'}
    json_data3 = {'name': 'Alice'}
    monkeypatch.setattr(os, 'listdir', MockedListDir(['file1.json', 'file2.json', 'file3.json']))
    monkeypatch.setattr(json, 'load', MockedJsonLoad(json_data1))
    result = task_func()
    assert result == {'Alice': 2, 'Bob': 1}

def test_task_func_multiple_json_files_with_different_keys(monkeypatch):
    json_data1 = {'name': 'Alice'}
    json_data2 = {'name': 'Bob'}
    json_data3 = {'age': 30}
    monkeypatch.setattr(os, 'listdir', MockedListDir(['file1.json', 'file2.json', 'file3.json']))
    monkeypatch.setattr(json, 'load', MockedJsonLoad(json_data1))
    result = task_func()
    assert result == {'Alice': 1}

def test_task_func_non_existent_key(monkeypatch):
    json_data = {'age': 30}
    monkeypatch.setattr(os, 'listdir', MockedListDir(['file1.json']))
    monkeypatch.setattr(json, 'load', MockedJsonLoad(json_data))
    result = task_func(key='name')
    assert result == {}