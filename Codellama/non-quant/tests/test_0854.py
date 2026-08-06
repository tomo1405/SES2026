import os

from src_0854 import task_func


def test_task_func():
    directory_path = 'test_directory'
    summary = task_func(directory_path)
    assert summary == {'Invalid': 0, 'txt': 1, 'jpg': 1, 'pdf': 1}

def test_task_func_invalid_characters():
    directory_path = 'test_directory'
    filename = 'test_file.txt'
    with open(os.path.join(directory_path, filename), 'w') as f:
        f.write('test_file')
    summary = task_func(directory_path)
    assert summary == {'Invalid': 1, 'txt': 0, 'jpg': 0, 'pdf': 0}

def test_task_func_invalid_extension():
    directory_path = 'test_directory'
    filename = 'test_file.txt'
    with open(os.path.join(directory_path, filename), 'w') as f:
        f.write('test_file')
    summary = task_func(directory_path)
    assert summary == {'Invalid': 1, 'txt': 0, 'jpg': 0, 'pdf': 0}

def test_task_func_invalid_directory():
    directory_path = 'test_directory'
    filename = 'test_file.txt'
    with open(os.path.join(directory_path, filename), 'w') as f:
        f.write('test_file')
    summary = task_func(directory_path)
    assert summary == {'Invalid': 1, 'txt': 0, 'jpg': 0, 'pdf': 0}