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

def test_task_func():
    dir = '/path/to/directory'
    api_key = 'your_api_key'
    recipient_email = 'recipient@example.com'
    with pytest.raises(FileNotFoundError):
        task_func(dir, api_key, recipient_email)
    dir = '/path/to/existing/directory'
    api_key = 'your_api_key'
    recipient_email = 'recipient@example.com'
    assert task_func(dir, api_key, recipient_email) == True