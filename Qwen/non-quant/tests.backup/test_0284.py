import pytest
from src_0284 import task_func
import os
import json
from collections import Counter

# Mocking os and json modules to avoid file I/O operations
class MockedList:
    def __init__(self, files):
        self.files = files

    def listdir(self, path):
        return self.files

class MockedOpen:
    def __init__(self, file_contents):
        self.file_contents = file_contents

    def __call__(self, file_path, mode='r'):
        return self

    def read(self):
        return json.dumps(self.file_contents)

@pytest.fixture
def mock_os(mocker):
    mocker.patch('os.listdir', new=MockedList(['file1.json', 'file2.json']).listdir)
    mocker.patch('builtins.open', new=MockedOpen({'name': 'Alice'}))

def test_task_func(mock_os):
    expected_output = {'Alice': 2}
    assert task_func() == expected_output

def test_task_func_with_different_key(mock_os):
    expected_output = {}
    assert task_func(key='age') == expected_output

def test_task_func_with_no_json_files(mock_os, mocker):
    mocker.patch('os.listdir', new=MockedList(['file1.txt', 'file2.txt']).listdir)
    expected_output = {}
    assert task_func() == expected_output

def test_task_func_with_empty_directory(mock_os, mocker):
    mocker.patch('os.listdir', new=MockedList([]).listdir)
    expected_output = {}
    assert task_func() == expected_output