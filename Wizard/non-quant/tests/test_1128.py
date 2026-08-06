python
import os
import re
import hashlib
import pytest

def task_func(path, delimiter):
    path_components = re.split(f'({delimiter})', path)
    hashes = []

    for component in path_components:
        if not component:  # Remove empty components
            continue
        if component != delimiter and os.path.isfile(component):
            with open(component, 'rb') as f:
                hashes.append(hashlib.sha256(f.read()).hexdigest())
        else:
            hashes.append(None)

    return list(zip(path_components, hashes))

def test_task_func():
    # Test case 1
    path = '/path/to/file1.txt'
    delimiter = '/'
    expected_result = [('path', None), ('to', None), ('file1.txt', '1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef')]
    assert task_func(path, delimiter) == expected_result

    # Test case 2
    path = '/path/to/file2.txt'
    delimiter = '/'
    expected_result = [('path', None), ('to', None), ('file2.txt', '234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef12')]
    assert task_func(path, delimiter) == expected_result

    # Test case 3
    path = '/path/to/dir1/file3.txt'
    delimiter = '/'
    expected_result = [('path', None), ('to', None), ('dir1', None), ('file3.txt', '34567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef123')]
    assert task_func(path, delimiter) == expected_result

    # Test case 4
    path = '/path/to/dir2/file4.txt'
    delimiter = '/'
    expected_result = [('path', None), ('to', None), ('dir2', None), ('file4.txt', '4567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234')]
    assert task_func(path, delimiter) == expected_result

    # Test case 5
    path = '/path/to/dir1/subdir1/file5.txt'
    delimiter = '/'
    expected_result = [('path', None), ('to', None), ('dir1', None), ('subdir1', None), ('file5.txt', '567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef12345')]
    assert task_func(path, delimiter) == expected_result

    # Test case 6
    path = '/path/to/dir2/subdir2/file6.txt'
    delimiter = '/'
    expected_result = [('path', None), ('to', None), ('dir2', None), ('subdir2', None), ('file6.txt', '67890abcdef1234567890abcdef1234567890abcdef1234567890abcdef123456')]
    assert task_func(path, delimiter) == expected_result

    # Test case 7
    path = '/path/to/dir1/subdir1/file5.txt'
    delimiter = '.'
    expected_result = [('path/to/dir1/subdir1/file5.txt', '567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef12345')]
    assert task_func(path, delimiter) == expected_result

    # Test case 8
    path = '/path/to/dir2/subdir2/file6.txt'
    delimiter = '.'
    expected_result = [('path/to/dir2/subdir2/file6.txt', '67890abcdef1234567890abcdef1234567890abcdef1234567890abcdef123456')]
    assert task_func(path, delimiter) == expected_result

    # Test case 9
    path = '/path/to/dir1/subdir1/file5.txt'
    delimiter = ' '
    expected_result = [('path/to/dir1/subdir1/file5.txt', '567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef12345')]
    assert task_func(path, delimiter) == expected_result

    # Test case 10
    path = '/path/to/dir2/subdir2/file6.txt'
    delimiter = ' '
    expected_result = [('path/to/dir2/subdir2/file6.txt', '67890abcdef1234567890abcdef1234567890abcdef1234567890abcdef123456')]
    assert task_func(path, delimiter) == expected_result

    # Test case 11
    path = '/path/to/dir1/subdir1/file5.txt'
    delimiter = ''
    expected_result = [('path', None), ('to', None), ('dir1', None), ('subdir1', None), ('file5.txt', '567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef12345')]
    assert task_func(path, delimiter) == expected_result

    # Test case 12
    path = '/path/to/dir2/subdir2/file6.txt'
    delimiter = ''
    expected_result = [('path', None), ('to', None), ('dir2', None), ('subdir2', None), ('file6.txt', '67890abcdef1234567890abcdef1234567890abcdef1234567890abcdef123456')]
    assert task_func(path, delimiter) == expected_result

    # Test case 13
    path = '/path/to/dir1/subdir1/file5.txt'
    delimiter = None
    expected_result = [('path', None), ('to', None), ('dir1', None), ('subdir1', None), ('file5.txt', '567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef12345')]
    assert task_func(path, delimiter) == expected_result

    # Test case 14
    path = '/path/to/dir2/subdir2/file6.txt'
    delimiter = None
    expected_result = [('path', None), ('to', None), ('dir2', None), ('subdir2', None), ('file6.txt', '67890abcdef1234567890abcdef1234567890abcdef1234567890abcdef123456')]
    assert task_func(path, delimiter) == expected_result