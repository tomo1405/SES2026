import sqlite3

import pytest
import requests
from src_1016 import task_func


def test_task_func_with_file_url():
    webpage_url = "file://path/to/file.html"
    num_rows_inserted = task_func(webpage_url)
    assert num_rows_inserted > 0

def test_task_func_with_valid_url():
    webpage_url = "https://www.example.com"
    num_rows_inserted = task_func(webpage_url)
    assert num_rows_inserted > 0

def test_task_func_with_invalid_url():
    webpage_url = "not_a_valid_url"
    with pytest.raises(requests.RequestException):
        task_func(webpage_url)

def test_task_func_with_invalid_database_name():
    webpage_url = "https://www.example.com"
    database_name = "not_a_valid_database.db"
    with pytest.raises(sqlite3.DatabaseError):
        task_func(webpage_url, database_name)