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
    # Test case 1: directory with no files
    directory = 'test_dir'
    os.mkdir(directory)
    assert task_func(directory) == []
    os.rmdir(directory)
    
    # Test case 2: directory with files with brackets in their names
    directory = 'test_dir'
    os.mkdir(directory)
    with open(os.path.join(directory, 'file1.txt'), 'w') as f:
        f.write('This is a file with brackets ({}).')
    with open(os.path.join(directory, 'file2.txt'), 'w') as f:
        f.write('This is a file with brackets [[]].')
    with open(os.path.join(directory, 'file3.txt'), 'w') as f:
        f.write('This is a file with brackets {{}}.')
    assert task_func(directory) == [os.path.join(directory, 'file1.txt'),
                                    os.path.join(directory, 'file2.txt'),
                                    os.path.join(directory, 'file3.txt')]
    os.remove(os.path.join(directory, 'file1.txt'))
    os.remove(os.path.join(directory, 'file2.txt'))
    os.remove(os.path.join(directory, 'file3.txt'))
    os.rmdir(directory)
    
    # Test case 3: directory with files without brackets in their names
    directory = 'test_dir'
    os.mkdir(directory)
    with open(os.path.join(directory, 'file1.txt'), 'w') as f:
        f.write('This is a file without brackets.')
    with open(os.path.join(directory, 'file2.txt'), 'w') as f:
        f.write('This is another file without brackets.')
    assert task_func(directory) == []
    os.remove(os.path.join(directory, 'file1.txt'))
    os.remove(os.path.join(directory, 'file2.txt'))
    os.rmdir(directory)