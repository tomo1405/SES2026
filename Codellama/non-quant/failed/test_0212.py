import pytest
from src_0212 import task_func

def test_task_func_with_valid_url():
    url = 'https://www.example.com/file.zip'
    destination_directory = '.'
    headers = {'accept': 'application/octet-stream'}

    extracted_files = task_func(url, destination_directory, headers)

    assert len(extracted_files) > 0
    assert all(os.path.isfile(os.path.join(destination_directory, file)) for file in extracted_files)

def test_task_func_with_invalid_url():
    url = 'https://www.example.com/file.zip'
    destination_directory = '.'
    headers = {'accept': 'application/octet-stream'}

    with pytest.raises(ValueError):
        task_func(url, destination_directory, headers)

def test_task_func_with_invalid_destination_directory():
    url = 'https://www.example.com/file.zip'
    destination_directory = '.'
    headers = {'accept': 'application/octet-stream'}

    with pytest.raises(ValueError):
        task_func(url, destination_directory, headers)

def test_task_func_with_invalid_headers():
    url = 'https://www.example.com/file.zip'
    destination_directory = '.'
    headers = {'accept': 'application/octet-stream'}

    with pytest.raises(ValueError):
        task_func(url, destination_directory, headers)