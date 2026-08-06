import codecs
import os
import glob
DIRECTORY_PATH = './files/'
def task_func(directory=DIRECTORY_PATH, from_encoding='cp1251', to_encoding='utf8'):
    for filename in glob.glob(os.path.join(directory, '*.txt')):
        with codecs.open(filename, 'r', from_encoding) as file:
            content = file.read()

        with codecs.open(filename, 'w', to_encoding) as file:
            file.write(content)
import pytest
def test_task_func():
    # Test case 1: Test if the function raises an exception when the directory does not exist
    with pytest.raises(FileNotFoundError):
        task_func(directory='nonexistent_directory')

    # Test case 2: Test if the function correctly converts files from cp1251 to utf8
    task_func()
    for filename in glob.glob(os.path.join(DIRECTORY_PATH, '*.txt')):
        with codecs.open(filename, 'r', 'utf8') as file:
            content = file.read()
        assert content.encoding == 'utf8'

    # Test case 3: Test if the function correctly converts files from utf8 to cp1251
    task_func(from_encoding='utf8', to_encoding='cp1251')
    for filename in glob.glob(os.path.join(DIRECTORY_PATH, '*.txt')):
        with codecs.open(filename, 'r', 'cp1251') as file:
            content = file.read()
        assert content.encoding == 'cp1251'