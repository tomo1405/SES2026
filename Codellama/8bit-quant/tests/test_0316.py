from unittest.mock import patch

import pytest
from src_0316 import task_func


def test_task_func_valid_dir():
    dir = 'test_dir'
    api_key = 'test_api_key'
    recipient_email = 'test@example.com'
    file_list = ['file1.txt', 'file2.txt']

    with patch('os.listdir', return_value=file_list):
        assert task_func(dir, api_key, recipient_email) == True

def test_task_func_invalid_dir():
    dir = 'invalid_dir'
    api_key = 'test_api_key'
    recipient_email = 'test@example.com'

    with pytest.raises(FileNotFoundError):
        task_func(dir, api_key, recipient_email)

def test_task_func_sendgrid_error():
    dir = 'test_dir'
    api_key = 'test_api_key'
    recipient_email = 'test@example.com'
    file_list = ['file1.txt', 'file2.txt']

    with patch('os.listdir', return_value=file_list):
        with patch('sendgrid.SendGridAPIClient.send', side_effect=HTTPError):
            with pytest.raises(HTTPError):
                task_func(dir, api_key, recipient_email)

def test_task_func_other_error():
    dir = 'test_dir'
    api_key = 'test_api_key'
    recipient_email = 'test@example.com'
    file_list = ['file1.txt', 'file2.txt']

    with patch('os.listdir', return_value=file_list):
        with patch('sendgrid.SendGridAPIClient.send', side_effect=Exception):
            with pytest.raises(Exception):
                task_func(dir, api_key, recipient_email)