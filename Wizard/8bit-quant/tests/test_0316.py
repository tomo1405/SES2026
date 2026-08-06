python
import os
import pytest
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

def test_task_func():
    # Test case 1: Directory exists
    with pytest.raises(FileNotFoundError):
        task_func('nonexistent_dir', 'api_key', 'recipient_email')

    # Test case 2: Directory does not exist
    with pytest.raises(FileNotFoundError):
        task_func('nonexistent_dir', 'api_key', 'recipient_email')

    # Test case 3: API key is invalid
    with pytest.raises(Exception):
        task_func('dir', 'invalid_api_key', 'recipient_email')

    # Test case 4: Email is invalid
    with pytest.raises(Exception):
        task_func('dir', 'api_key', 'invalid_email')

    # Test case 5: Email is valid
    assert task_func('dir', 'api_key', 'recipient_email') == True