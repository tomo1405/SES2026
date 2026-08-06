import pytest
from src_0316 import task_func


def test_task_func_valid_dir():
    dir = 'path/to/directory'
    api_key = 'your_api_key'
    recipient_email = 'recipient@example.com'
    file_list = ['file1.txt', 'file2.txt']

    with pytest.raises(FileNotFoundError):
        task_func(dir, api_key, recipient_email)

    with pytest.raises(HTTPError):
        task_func(dir, api_key, recipient_email)

    with pytest.raises(Exception):
        task_func(dir, api_key, recipient_email)

def test_task_func_invalid_dir():
    dir = 'path/to/invalid/directory'
    api_key = 'your_api_key'
    recipient_email = 'recipient@example.com'

    with pytest.raises(FileNotFoundError):
        task_func(dir, api_key, recipient_email)

def test_task_func_invalid_api_key():
    dir = 'path/to/directory'
    api_key = 'invalid_api_key'
    recipient_email = 'recipient@example.com'

    with pytest.raises(HTTPError):
        task_func(dir, api_key, recipient_email)

def test_task_func_invalid_recipient_email():
    dir = 'path/to/directory'
    api_key = 'your_api_key'
    recipient_email = 'invalid_recipient_email'

    with pytest.raises(Exception):
        task_func(dir, api_key, recipient_email)