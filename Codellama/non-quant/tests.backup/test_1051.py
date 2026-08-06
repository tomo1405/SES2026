import pytest
from src_1051 import task_func

def test_task_func():
    input_string = "Hello\nWorld\n"
    expected_file_paths = [
        "./hashed_files/1234567890.txt",
        "./hashed_files/abcdef0123.txt"
    ]

    file_paths = task_func(input_string)

    assert len(file_paths) == len(expected_file_paths)
    for file_path in file_paths:
        assert os.path.exists(file_path)
        with open(file_path, "r", encoding="utf-8") as file:
            assert file.read() == os.path.basename(file_path)