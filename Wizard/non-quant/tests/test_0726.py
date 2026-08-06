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
    # Test case 1: Default parameters
    task_func()
    assert os.path.isfile(os.path.join(DIRECTORY_PATH, 'test.txt'))
    with codecs.open(os.path.join(DIRECTORY_PATH, 'test.txt'), 'r', 'utf8') as file:
        assert file.read() == 'тест'

    # Test case 2: Custom parameters
    task_func(directory='./files2/', from_encoding='utf8', to_encoding='cp1251')
    assert os.path.isfile(os.path.join('./files2/', 'test.txt'))
    with codecs.open(os.path.join('./files2/', 'test.txt'), 'r', 'cp1251') as file:
        assert file.read() == 'тест'

    # Test case 3: Non-existent directory
    with pytest.raises(FileNotFoundError):
        task_func(directory='./nonexistent/')

    # Test case 4: Non-existent encoding
    with pytest.raises(LookupError):
        task_func(from_encoding='nonexistent', to_encoding='utf8')