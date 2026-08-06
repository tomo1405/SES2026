import os
import re
import hashlib
from src_1128 import task_func
def test_task_func():
    path = '/path/to/file.txt'
    delimiter = '/'
    expected_output = [
        (path, hashlib.sha256(open(path, 'rb').read()).hexdigest()),
        ('to', None),
        ('path', None),
        ('file.txt', None)
    ]
    assert task_func(path, delimiter) == expected_output
def test_task_func_with_multiple_delimiters():
    path = '/path/to/file.txt'
    delimiter = '/'
    expected_output = [
        (path, hashlib.sha256(open(path, 'rb').read()).hexdigest()),
        ('to', None),
        ('path', None),
        ('file.txt', None)
    ]
    assert task_func(path, delimiter) == expected_output
def test_task_func_with_no_delimiter():
    path = '/path/to/file.txt'
    delimiter = ''
    expected_output = [
        (path, hashlib.sha256(open(path, 'rb').read()).hexdigest()),
        ('to', None),
        ('path', None),
        ('file.txt', None)
    ]
    assert task_func(path, delimiter) == expected_output