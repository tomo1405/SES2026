import csv
import os
import tempfile

import pytest
import requests
from src_1137 import task_func


@pytest.fixture
def temp_csv_file():
    fd, path = tempfile.mkstemp(suffix='.csv')
    os.close(fd)
    yield path
    os.remove(path)

def test_task_func_with_default_params(temp_csv_file):
    url = "http://example.com"
    csv_path = temp_csv_file
    result = task_func(url, csv_path)
    assert result == csv_path
    assert os.path.exists(csv_path)

def test_task_func_with_custom_regex(temp_csv_file):
    url = "http://example.com"
    csv_path = temp_csv_file
    custom_regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"
    result = task_func(url, csv_path, regex=custom_regex)
    assert result == csv_path
    assert os.path.exists(csv_path)

def test_task_func_with_nonexistent_url(temp_csv_file):
    url = "http://nonexistenturl.com"
    csv_path = temp_csv_file
    with pytest.raises(requests.exceptions.RequestException):
        task_func(url, csv_path)

def test_task_func_with_no_emails_found(temp_csv_file):
    url = "http://example.com"
    csv_path = temp_csv_file
    # Assuming the example.com does not contain any emails
    result = task_func(url, csv_path)
    assert result == csv_path
    assert os.path.exists(csv_path)
    with open(csv_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)
    assert len(rows) == 1  # Only the header row should exist

def test_task_func_with_invalid_csv_path():
    url = "http://example.com"
    csv_path = "/invalid/path/to/file.csv"
    with pytest.raises(FileNotFoundError):
        task_func(url, csv_path)