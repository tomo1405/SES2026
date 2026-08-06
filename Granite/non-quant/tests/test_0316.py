import pytest
from src_0316 import task_func


def test_task_func():
    dir = '/path/to/directory'
    api_key = 'your_sendgrid_api_key'
    recipient_email = 'recipient@example.com'

    with pytest.raises(FileNotFoundError):
        task_func(dir='invalid_directory_path', api_key=api_key, recipient_email=recipient_email)

    with pytest.raises(HTTPError):
        task_func(dir=dir, api_key='invalid_api_key', recipient_email=recipient_email)

    with pytest.raises(Exception):
        task_func(dir=dir, api_key=api_key, recipient_email=recipient_email)

    assert task_func(dir=dir, api_key=api_key, recipient_email=recipient_email) == 200