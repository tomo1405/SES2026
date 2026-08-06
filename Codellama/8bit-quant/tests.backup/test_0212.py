import pytest
from src_0212 import task_func

def test_task_func_valid_url():
    url = 'https://www.example.com/file.zip'
    destination_directory = '.'
    headers = {'accept': 'application/octet-stream'}
    expected_files = ['file.zip']

    files = task_func(url, destination_directory, headers)

    assert files == expected_files

def test_task_func_invalid_url():
    url = 'https://www.example.com/file.zip'
    destination_directory = '.'
    headers = {'accept': 'application/octet-stream'}
    expected_files = []

    files = task_func(url, destination_directory, headers)

    assert files == expected_files

def test_task_func_invalid_headers():
    url = 'https://www.example.com/file.zip'
    destination_directory = '.'
    headers = {'accept': 'application/json'}
    expected_files = []

    files = task_func(url, destination_directory, headers)

    assert files == expected_files