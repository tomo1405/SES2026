import codecs
import os
import glob
import pytest
from src_0726 import task_func

DIRECTORY_PATH = './files/'

def test_task_func():
    # Test case 1: Test if the function runs without any errors
    task_func()

    # Test case 2: Test if the function converts files from cp1251 encoding to utf8 encoding
    task_func(from_encoding='cp1251', to_encoding='utf8')
    for filename in glob.glob(os.path.join(DIRECTORY_PATH, '*.txt')):
        with codecs.open(filename, 'r', 'utf8') as file:
            content = file.read()
        assert content.startswith(codecs.BOM_UTF8)

    # Test case 3: Test if the function converts files from cp1251 encoding to utf-16 encoding
    task_func(from_encoding='cp1251', to_encoding='utf-16')
    for filename in glob.glob(os.path.join(DIRECTORY_PATH, '*.txt')):
        with codecs.open(filename, 'r', 'utf-16') as file:
            content = file.read()
        assert content.startswith(codecs.BOM_UTF16)

    # Test case 4: Test if the function raises an error when an invalid encoding is provided
    with pytest.raises(LookupError):
        task_func(from_encoding='invalid_encoding', to_encoding='utf8')