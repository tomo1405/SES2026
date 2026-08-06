python
import codecs
import os
import glob
import pytest

# Constants
DIRECTORY_PATH = './files/'

def task_func(directory=DIRECTORY_PATH, from_encoding='cp1251', to_encoding='utf8'):
    for filename in glob.glob(os.path.join(directory, '*.txt')):
        with codecs.open(filename, 'r', from_encoding) as file:
            content = file.read()

        with codecs.open(filename, 'w', to_encoding) as file:
            file.write(content)

def test_task_func():
    # Test case 1: Convert all files in the directory to utf-8 encoding
    task_func(directory=DIRECTORY_PATH, from_encoding='cp1251', to_encoding='utf8')
    # Test case 2: Convert all files in the directory to cp1251 encoding
    task_func(directory=DIRECTORY_PATH, from_encoding='utf8', to_encoding='cp1251')
    # Test case 3: Convert all files in a different directory to utf-8 encoding
    task_func(directory='./other_directory/', from_encoding='cp1251', to_encoding='utf8')
    # Test case 4: Convert all files in a different directory to cp1251 encoding
    task_func(directory='./other_directory/', from_encoding='utf8', to_encoding='cp1251')