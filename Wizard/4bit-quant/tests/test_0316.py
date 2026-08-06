python
import os
import pytest
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from python_http_client.exceptions import HTTPError
from src_0316 import task_func

def test_task_func_valid_dir():
    # Test valid directory
    dir = '/path/to/directory'
    api_key = 'api_key'
    recipient_email = 'recipient_email@example.com'
    assert task_func(dir, api_key, recipient_email)

def test_task_func_invalid_dir():
    # Test invalid directory
    dir = '/path/to/invalid/directory'
    api_key = 'api_key'
    recipient_email = 'recipient_email@example.com'
    with pytest.raises(FileNotFoundError):
        task_func(dir, api_key, recipient_email)

def test_task_func_valid_api_key():
    # Test valid API key
    dir = '/path/to/directory'
    api_key = 'api_key'
    recipient_email = 'recipient_email@example.com'
    assert task_func(dir, api_key, recipient_email)

def test_task_func_invalid_api_key():
    # Test invalid API key
    dir = '/path/to/directory'
    api_key = 'invalid_api_key'
    recipient_email = 'recipient_email@example.com'
    with pytest.raises(Exception):
        task_func(dir, api_key, recipient_email)

def test_task_func_valid_recipient_email():
    # Test valid recipient email
    dir = '/path/to/directory'
    api_key = 'api_key'
    recipient_email = 'recipient_email@example.com'
    assert task_func(dir, api_key, recipient_email)

def test_task_func_invalid_recipient_email():
    # Test invalid recipient email
    dir = '/path/to/directory'
    api_key = 'api_key'
    recipient_email = 'invalid_recipient_email@example.com'
    with pytest.raises(Exception):
        task_func(dir, api_key, recipient_email)