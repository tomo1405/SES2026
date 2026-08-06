import pytest
from src_0714 import task_func

def test_task_func():
    log_file_path = "path/to/log/file"
    keywords = ["keyword1", "keyword2"]
    formatted_lines = task_func(log_file_path, keywords)
    assert formatted_lines == [
        "keyword1 : value1 : value2",
        "keyword2 : value3 : value4"
    ]

def test_task_func_invalid_log_file():
    log_file_path = "path/to/invalid/log/file"
    keywords = ["keyword1", "keyword2"]
    with pytest.raises(FileNotFoundError):
        task_func(log_file_path, keywords)

def test_task_func_invalid_keywords():
    log_file_path = "path/to/log/file"
    keywords = ["keyword1", "keyword2"]
    formatted_lines = task_func(log_file_path, keywords)
    assert formatted_lines == [
        "keyword1 : value1 : value2",
        "keyword2 : value3 : value4"
    ]

def test_task_func_invalid_line_format():
    log_file_path = "path/to/log/file"
    keywords = ["keyword1", "keyword2"]
    formatted_lines = task_func(log_file_path, keywords)
    assert formatted_lines == [
        "keyword1 : value1 : value2",
        "keyword2 : value3 : value4"
    ]