import os
import re
import hashlib
from src_1128 import task_func
def test_task_func():
    path = '/path/to/file.txt'
    delimiter = '/'
    expected_output = [('path', None), ('to', None), ('file.txt', '5f4dcc3b5aa765d61d8327deb882cf99f333699072492152b5783c63400c6242')]
    output = task_func(path, delimiter)
    assert output == expected_output
def test_task_func_with_multiple_files():
    path = '/path/to/file1.txt/file2.txt'
    delimiter = '/'
    expected_output = [('path', None), ('to', None), ('file1.txt', '5f4dcc3b5aa765d61d8327deb882cf99f333699072492152b5783c63400c6242'), ('file2.txt', '5f4dcc3b5aa765d61d8327deb882cf99f333699072492152b5783c63400c6242')]
    output = task_func(path, delimiter)
    assert output == expected_output
def test_task_func_with_no_files():
    path = '/path/to/directory/'
    delimiter = '/'
    expected_output = [('path', None), ('to', None), ('directory', None), ('', None)]
    output = task_func(path, delimiter)
    assert output == expected_output