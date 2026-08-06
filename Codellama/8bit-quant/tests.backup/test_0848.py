import pytest
from src_0848 import task_func

def test_task_func():
    input_string = "This is a test string\nThis is another test string"
    directory = "./text_files"
    file_paths = task_func(input_string, directory)
    assert len(file_paths) == 2
    assert all(os.path.isfile(file_path) for file_path in file_paths)
    assert all(os.path.join(directory, file_path) == file_path for file_path in file_paths)
    for file_path in file_paths:
        with open(file_path, 'r') as file:
            assert file.read() == input_string.split('\n')[int(file_path.split('.')[0])]