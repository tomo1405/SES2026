import pytest
from src_0282 import task_func
import os
from collections import Counter

# Mocking os and re modules for testing
class MockFile:
    def __init__(self, content):
        self.content = content

    def read(self):
        return self.content

class MockOS:
    @staticmethod
    def listdir(path):
        return ['file1.log', 'file2.log', 'not_a_log.txt']

    @staticmethod
    def path.join(folder_path, filename):
        return os.path.join(folder_path, filename)

class MockRe:
    @staticmethod
    def compile(pattern):
        return re.compile(pattern)

    @staticmethod
    def findall(regex, string):
        return ['192.168.1.1', '192.168.1.2'] if regex.pattern == '\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}' else []

@pytest.fixture
def mock_os(monkeypatch):
    monkeypatch.setattr(os, 'listdir', MockOS.listdir)
    monkeypatch.setattr(os.path, 'join', MockOS.path.join)

@pytest.fixture
def mock_re(monkeypatch):
    monkeypatch.setattr(re, 'compile', MockRe.compile)
    monkeypatch.setattr(re, 'findall', MockRe.findall)

@pytest.fixture
def mock_open(monkeypatch):
    def mock_open_func(file_path, mode='r'):
        if file_path.endswith('file1.log'):
            return MockFile("Log entry with IP 192.168.1.1")
        elif file_path.endswith('file2.log'):
            return MockFile("Log entry with IP 192.168.1.2 and another IP 192.168.1.1")
        else:
            raise FileNotFoundError
    monkeypatch.setattr('builtins.open', mock_open_func)

def test_task_func(mock_os, mock_re, mock_open):
    folder_path = '/path/to/logs'
    result = task_func(folder_path)
    expected_result = {'192.168.1.1': 2, '192.168.1.2': 1}
    assert result == expected_result