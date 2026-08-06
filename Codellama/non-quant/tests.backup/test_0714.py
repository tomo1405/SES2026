import pytest
from src_0714 import task_func

def test_task_func_valid_input():
    log_file_path = "test_log.txt"
    keywords = ["keyword1", "keyword2"]
    expected_output = [
        "keyword1 : value1 : value2",
        "keyword2 : value3 : value4"
    ]
    with open(log_file_path, "w") as log:
        log.write("keyword1 value1 value2\n")
        log.write("keyword2 value3 value4\n")
    assert task_func(log_file_path, keywords) == expected_output

def test_task_func_invalid_input():
    log_file_path = "test_log.txt"
    keywords = ["keyword1", "keyword2"]
    with open(log_file_path, "w") as log:
        log.write("invalid line\n")
    with pytest.raises(ValueError):
        task_func(log_file_path, keywords)

def test_task_func_missing_file():
    log_file_path = "missing_file.txt"
    keywords = ["keyword1", "keyword2"]
    with pytest.raises(FileNotFoundError):
        task_func(log_file_path, keywords)