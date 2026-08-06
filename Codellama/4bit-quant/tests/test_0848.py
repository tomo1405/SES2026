import pytest
from src_0848 import task_func

def test_task_func():
    input_string = "This is a test string\nThis is another test string"
    directory = "./text_files"
    file_paths = task_func(input_string, directory)
    assert len(file_paths) == 2
    for file_path in file_paths:
        assert os.path.isfile(file_path)
        with open(file_path, 'r') as file:
            assert file.read() == "This is a test string" or file.read() == "This is another test string"
    os.remove(file_paths[0])
    os.remove(file_paths[1])