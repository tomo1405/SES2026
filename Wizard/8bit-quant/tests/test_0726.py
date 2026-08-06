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
    # Test case 1: Test with default parameters
    task_func()
    assert os.path.isfile(os.path.join(DIRECTORY_PATH, 'test1.txt'))
    assert os.path.isfile(os.path.join(DIRECTORY_PATH, 'test2.txt'))
    assert os.path.isfile(os.path.join(DIRECTORY_PATH, 'test3.txt'))
    os.remove(os.path.join(DIRECTORY_PATH, 'test1.txt'))
    os.remove(os.path.join(DIRECTORY_PATH, 'test2.txt'))
    os.remove(os.path.join(DIRECTORY_PATH, 'test3.txt'))

    # Test case 2: Test with custom parameters
    task_func(directory='./files2/', from_encoding='utf8', to_encoding='cp1251')
    assert os.path.isfile(os.path.join('./files2/', 'test1.txt'))
    assert os.path.isfile(os.path.join('./files2/', 'test2.txt'))
    assert os.path.isfile(os.path.join('./files2/', 'test3.txt'))
    os.remove(os.path.join('./files2/', 'test1.txt'))
    os.remove(os.path.join('./files2/', 'test2.txt'))
    os.remove(os.path.join('./files2/', 'test3.txt'))

    # Test case 3: Test with non-existent directory
    with pytest.raises(FileNotFoundError):
        task_func(directory='./nonexistent/')

    # Test case 4: Test with non-existent encoding
    with pytest.raises(LookupError):
        task_func(from_encoding='nonexistent', to_encoding='utf8')