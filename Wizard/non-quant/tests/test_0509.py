python
import hashlib
import io
import os
import pytest

def task_func(file_path1, file_path2):
    if not os.path.exists(file_path1) or not os.path.exists(file_path2):
        raise FileNotFoundError("File not found! Please specify a valid filepath")

    with io.open(file_path1, 'rb') as file1, io.open(file_path2, 'rb') as file2:
        file1_hash = hashlib.md5(file1.read()).hexdigest()
        file2_hash = hashlib.md5(file2.read()).hexdigest()

    return file1_hash == file2_hash

def test_task_func():
    # Test case 1: Both files exist and have the same content
    file_path1 = "test_file1.txt"
    file_path2 = "test_file2.txt"
    with open(file_path1, "w") as f:
        f.write("Hello, world!")
    with open(file_path2, "w") as f:
        f.write("Hello, world!")
    assert task_func(file_path1, file_path2) == True
    os.remove(file_path1)
    os.remove(file_path2)

    # Test case 2: Both files exist but have different content
    file_path1 = "test_file1.txt"
    file_path2 = "test_file2.txt"
    with open(file_path1, "w") as f:
        f.write("Hello, world!")
    with open(file_path2, "w") as f:
        f.write("Goodbye, world!")
    assert task_func(file_path1, file_path2) == False
    os.remove(file_path1)
    os.remove(file_path2)

    # Test case 3: One of the files does not exist
    file_path1 = "test_file1.txt"
    file_path2 = "test_file2.txt"
    with open(file_path1, "w") as f:
        f.write("Hello, world!")
    with pytest.raises(FileNotFoundError):
        task_func(file_path1, "non_existent_file.txt")
    os.remove(file_path1)