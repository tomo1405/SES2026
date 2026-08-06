import pytest
from src_0511 import task_func

def test_task_func():
    file_path1 = 'file1.txt'
    file_path2 = 'file2.txt'
    with open(file_path1, 'w') as file1, open(file_path2, 'w') as file2:
        file1.write('Hello, World!')
        file2.write('Hello, World!')

    diff = task_func(file_path1, file_path2)
    assert diff == ''

def test_task_func_diff():
    file_path1 = 'file1.txt'
    file_path2 = 'file2.txt'
    with open(file_path1, 'w') as file1, open(file_path2, 'w') as file2:
        file1.write('Hello, World!')
        file2.write('Hello, Universe!')

    diff = task_func(file_path1, file_path2)
    assert diff == '+ Hello, Universe!\n- Hello, World!'