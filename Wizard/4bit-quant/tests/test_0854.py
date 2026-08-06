python
import os
import shutil
import string
import pytest

# Constants
INVALID_CHARACTERS = string.punctuation + string.whitespace

def task_func(directory_path):
    summary = {}
    for filename in os.listdir(directory_path):
        if any(char in INVALID_CHARACTERS for char in filename):
            if not os.path.exists(os.path.join(directory_path, 'Invalid')):
                os.mkdir(os.path.join(directory_path, 'Invalid'))
            shutil.move(os.path.join(directory_path, filename), os.path.join(directory_path, 'Invalid'))
            summary['Invalid'] = summary.get('Invalid', 0) + 1
        else:
            extension = os.path.splitext(filename)[-1].strip('.')
            if not os.path.exists(os.path.join(directory_path, extension)):
                os.mkdir(os.path.join(directory_path, extension))
            shutil.move(os.path.join(directory_path, filename), os.path.join(directory_path, extension))
            summary[extension] = summary.get(extension, 0) + 1
    return summary

def test_task_func():
    # Test case 1: Valid directory
    directory_path = 'test_dir'
    os.mkdir(directory_path)
    with open(os.path.join(directory_path, 'file1.txt'), 'w') as f:
        f.write('Test file 1')
    with open(os.path.join(directory_path, 'file2.txt'), 'w') as f:
        f.write('Test file 2')
    with open(os.path.join(directory_path, 'file3.txt'), 'w') as f:
        f.write('Test file 3')
    summary = task_func(directory_path)
    assert summary == {'txt': 3}
    assert os.path.exists(os.path.join(directory_path, 'txt'))
    assert os.path.exists(os.path.join(directory_path, 'file1.txt'))
    assert os.path.exists(os.path.join(directory_path, 'file2.txt'))
    assert os.path.exists(os.path.join(directory_path, 'file3.txt'))
    assert not os.path.exists(os.path.join(directory_path, 'Invalid'))
    assert not os.path.exists(os.path.join(directory_path, 'file1.txt'))
    assert not os.path.exists(os.path.join(directory_path, 'file2.txt'))
    assert not os.path.exists(os.path.join(directory_path, 'file3.txt'))
    os.rmdir(directory_path)

    # Test case 2: Directory with invalid characters
    directory_path = 'test_dir'
    os.mkdir(directory_path)
    with open(os.path.join(directory_path, 'file1.txt'), 'w') as f:
        f.write('Test file 1')
    with open(os.path.join(directory_path, 'file2.txt'), 'w') as f:
        f.write('Test file 2')
    with open(os.path.join(directory_path, 'file3.txt'), 'w') as f:
        f.write('Test file 3')
    with open(os.path.join(directory_path, 'file4.txt!'), 'w') as f:
        f.write('Test file 4')
    summary = task_func(directory_path)
    assert summary == {'txt': 3, 'Invalid': 1}
    assert os.path.exists(os.path.join(directory_path, 'txt'))
    assert os.path.exists(os.path.join(directory_path, 'file1.txt'))
    assert os.path.exists(os.path.join(directory_path, 'file2.txt'))
    assert os.path.exists(os.path.join(directory_path, 'file3.txt'))
    assert os.path.exists(os.path.join(directory_path, 'Invalid'))
    assert os.path.exists(os.path.join(directory_path, 'file4.txt!'))
    assert not os.path.exists(os.path.join(directory_path, 'file1.txt'))
    assert not os.path.exists(os.path.join(directory_path, 'file2.txt'))
    assert not os.path.exists(os.path.join(directory_path, 'file3.txt'))
    assert not os.path.exists(os.path.join(directory_path, 'file4.txt!'))
    os.rmdir(directory_path)

    # Test case 3: Directory with no files
    directory_path = 'test_dir'
    os.mkdir(directory_path)
    summary = task_func(directory_path)
    assert summary == {}
    assert not os.path.exists(os.path.join(directory_path, 'txt'))
    assert not os.path.exists(os.path.join(directory_path, 'Invalid'))
    os.rmdir(directory_path)

    # Test case 4: Directory with no valid files
    directory_path = 'test_dir'
    os.mkdir(directory_path)
    with open(os.path.join(directory_path, 'file1.txt'), 'w') as f:
        f.write('Test file 1')
    with open(os.path.join(directory_path, 'file2.txt'), 'w') as f:
        f.write('Test file 2')
    with open(os.path.join(directory_path, 'file3.txt'), 'w') as f:
        f.write('Test file 3')
    with open(os.path.join(directory_path, 'file4.txt!'), 'w') as f:
        f.write('Test file 4')
    summary = task_func(directory_path)
    assert summary == {'Invalid': 4}
    assert os.path.exists(os.path.join(directory_path, 'Invalid'))
    assert os.path.exists(os.path.join(directory_path, 'file1.txt'))
    assert os.path.exists(os.path.join(directory_path, 'file2.txt'))
    assert os.path.exists(os.path.join(directory_path, 'file3.txt'))
    assert os.path.exists(os.path.join(directory_path, 'file4.txt!'))
    assert not os.path.exists(os.path.join(directory_path, 'txt'))
    os.rmdir(directory_path)