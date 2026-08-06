import pytest
from src_1128 import task_func

# Mocking os.path.isfile to control file existence
class MockPath:
    @staticmethod
    def isfile(path):
        return path in ['file1.txt', 'file2.txt']

# Mocking hashlib.sha256 to control hash values
class MockHash:
    def __init__(self, data):
        self.data = data

    def update(self, data):
        pass

    def hexdigest(self):
        if self.data == b'content of file1':
            return 'hash1'
        elif self.data == b'content of file2':
            return 'hash2'
        return None

# Patching os.path and hashlib for testing
import os
import hashlib
os.path = MockPath()
hashlib.sha256 = lambda data: MockHash(data)

def test_task_func_with_files():
    path = 'path/to/file1.txt/path/to/file2.txt'
    delimiter = '/'
    expected_output = [
        ('path', None),
        ('/', None),
        ('to', None),
        ('/', None),
        ('file1.txt', 'hash1'),
        ('/', None),
        ('path', None),
        ('/', None),
        ('to', None),
        ('/', None),
        ('file2.txt', 'hash2')
    ]
    assert task_func(path, delimiter) == expected_output

def test_task_func_without_files():
    path = 'path/to/nonexistentfile.txt/path/to/anotherfile.txt'
    delimiter = '/'
    expected_output = [
        ('path', None),
        ('/', None),
        ('to', None),
        ('/', None),
        ('nonexistentfile.txt', None),
        ('/', None),
        ('path', None),
        ('/', None),
        ('to', None),
        ('/', None),
        ('anotherfile.txt', None)
    ]
    assert task_func(path, delimiter) == expected_output

def test_task_func_empty_path():
    path = ''
    delimiter = '/'
    expected_output = []
    assert task_func(path, delimiter) == expected_output

def test_task_func_no_delimiter_in_path():
    path = 'file1.txtfile2.txt'
    delimiter = '/'
    expected_output = [
        ('file1.txtfile2.txt', None)
    ]
    assert task_func(path, delimiter) == expected_output

def test_task_func_with_trailing_delimiter():
    path = 'path/to/file1.txt/'
    delimiter = '/'
    expected_output = [
        ('path', None),
        ('/', None),
        ('to', None),
        ('/', None),
        ('file1.txt', 'hash1'),
        ('/', None)
    ]
    assert task_func(path, delimiter) == expected_output