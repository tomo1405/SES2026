python
import os
import re
import pytest

def task_func(directory):
    BRACKET_PATTERN = '[(){}\\[\\]]'  # Corrected pattern to match any type of bracket
    
    file_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if re.search(BRACKET_PATTERN, file):
                file_list.append(os.path.join(root, file))
    return file_list

def test_task_func():
    # Test case 1
    directory = 'test_dir'
    os.makedirs(directory)
    with open(os.path.join(directory, 'test_file.txt'), 'w') as f:
        f.write('This is a test file with brackets (){}[]')
    assert task_func(directory) == [os.path.join(directory, 'test_file.txt')]
    os.remove(os.path.join(directory, 'test_file.txt'))
    os.rmdir(directory)

    # Test case 2
    directory = 'test_dir'
    os.makedirs(directory)
    with open(os.path.join(directory, 'test_file.txt'), 'w') as f:
        f.write('This is a test file with no brackets')
    assert task_func(directory) == []
    os.remove(os.path.join(directory, 'test_file.txt'))
    os.rmdir(directory)

    # Test case 3
    directory = 'test_dir'
    os.makedirs(directory)
    with open(os.path.join(directory, 'test_file.txt'), 'w') as f:
        f.write('This is a test file with brackets (){}[]')
    with open(os.path.join(directory, 'test_file2.txt'), 'w') as f:
        f.write('This is a test file with brackets (){}[]')
    assert task_func(directory) == [os.path.join(directory, 'test_file.txt'), os.path.join(directory, 'test_file2.txt')]
    os.remove(os.path.join(directory, 'test_file.txt'))
    os.remove(os.path.join(directory, 'test_file2.txt'))
    os.rmdir(directory)