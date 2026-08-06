import pytest
from src_0854 import task_func

def test_task_func():
    directory_path = 'test_directory'
    summary = task_func(directory_path)
    assert summary == {'Invalid': 0, 'txt': 0, 'jpg': 0, 'pdf': 0}

def test_task_func_invalid_characters():
    directory_path = 'test_directory'
    filename = 'test_file.txt'
    with open(os.path.join(directory_path, filename), 'w') as f:
        f.write('test')
    summary = task_func(directory_path)
    assert summary == {'Invalid': 1, 'txt': 0, 'jpg': 0, 'pdf': 0}

def test_task_func_invalid_extension():
    directory_path = 'test_directory'
    filename = 'test_file.txt'
    with open(os.path.join(directory_path, filename), 'w') as f:
        f.write('test')
    summary = task_func(directory_path)
    assert summary == {'Invalid': 0, 'txt': 1, 'jpg': 0, 'pdf': 0}

def test_task_func_multiple_files():
    directory_path = 'test_directory'
    filenames = ['test_file1.txt', 'test_file2.jpg', 'test_file3.pdf']
    for filename in filenames:
        with open(os.path.join(directory_path, filename), 'w') as f:
            f.write('test')
    summary = task_func(directory_path)
    assert summary == {'Invalid': 0, 'txt': 1, 'jpg': 1, 'pdf': 1}