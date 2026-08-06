import pytest
from src_1016 import task_func

def test_task_func_with_file_url():
    webpage_url = "file://path/to/file.html"
    num_records = task_func(webpage_url)
    assert num_records == expected_num_records

def test_task_func_with_http_url():
    webpage_url = "http://www.example.com"
    num_records = task_func(webpage_url)
    assert num_records == expected_num_records

def test_task_func_with_invalid_url():
    webpage_url = "not_a_valid_url"
    with pytest.raises(requests.RequestException):
        task_func(webpage_url)

def test_task_func_with_empty_data():
    webpage_url = "file://path/to/empty_file.html"
    num_records = task_func(webpage_url)
    assert num_records == 0

def test_task_func_with_invalid_database_name():
    webpage_url = "http://www.example.com"
    database_name = "not/a/valid/path"
    with pytest.raises(sqlite3.DatabaseError):
        task_func(webpage_url, database_name)