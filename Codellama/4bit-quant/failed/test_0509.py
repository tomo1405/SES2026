import pytest
from src_0509 import task_func

def test_task_func():
    file_path1 = "file1.txt"
    file_path2 = "file2.txt"
    with open(file_path1, 'w') as f:
        f.write("Hello")
    with open(file_path2, 'w') as f:
        f.write("Hello")
    assert task_func(file_path1, file_path2) == True

def test_task_func_invalid_file():
    file_path1 = "file1.txt"
    file_path2 = "file2.txt"
    with open(file_path1, 'w') as f:
        f.write("Hello")
    with open(file_path2, 'w') as f:
        f.write("World")
    with pytest.raises(FileNotFoundError):
        task_func(file_path1, file_path2)