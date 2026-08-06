import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from python_http_client.exceptions import HTTPError
def task_func(dir, api_key, recipient_email):
    try:
        file_list = os.listdir(dir)
    except:
        raise FileNotFoundError(f"Directory '{dir}' does not exist.")

    file_list_str = ', '.join(file_list)

    message = Mail(
        from_email='from_email@example.com',
        to_emails=recipient_email,
        subject=f'Directory Listing for {dir}',
        plain_text_content=file_list_str)

    try:
        sg = SendGridAPIClient(api_key)
        response = sg.send(message)
        # Assuming success codes are in the 2xx range
        return 200 <= response.status_code < 300
    except HTTPError as e:
        print(f"HTTP error occurred: {e}")
        raise
    except Exception as e:
        print(f"An error occurred: {e}")
        raise
import pytest
def test_task_func_with_valid_directory():
    dir = '/path/to/valid/directory'
    api_key = 'valid_api_key'
    recipient_email = 'recipient@example.com'
    with pytest.raises(FileNotFoundError):
        task_func(dir, api_key, recipient_email)
def test_task_func_with_invalid_directory():
    dir = '/path/to/invalid/directory'
    api_key = 'valid_api_key'
    recipient_email = 'recipient@example.com'
    with pytest.raises(FileNotFoundError):
        task_func(dir, api_key, recipient_email)
def test_task_func_with_valid_api_key():
    dir = '/path/to/valid/directory'
    api_key = 'valid_api_key'
    recipient_email = 'recipient@example.com'
    assert task_func(dir, api_key, recipient_email)
def test_task_func_with_invalid_api_key():
    dir = '/path/to/valid/directory'
    api_key = 'invalid_api_key'
    recipient_email = 'recipient@example.com'
    with pytest.raises(HTTPError):
        task_func(dir, api_key, recipient_email)
def test_task_func_with_valid_recipient_email():
    dir = '/path/to/valid/directory'
    api_key = 'valid_api_key'
    recipient_email = 'recipient@example.com'
    assert task_func(dir, api_key, recipient_email)
def test_task_func_with_invalid_recipient_email():
    dir = '/path/to/valid/directory'
    api_key = 'valid_api_key'
    recipient_email = 'invalid_recipient@example.com'
    with pytest.raises(HTTPError):
        task_func(dir, api_key, recipient_email)