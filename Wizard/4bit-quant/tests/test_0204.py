python
import json
import smtplib
import pytest

# Constants
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = "your.email@gmail.com"
EMAIL_PASSWORD = "your.password"

def task_func(input_data=None, smtp_server=SMTP_SERVER, smtp_port=SMTP_PORT, email_address=EMAIL_ADDRESS, email_password=EMAIL_PASSWORD, smtp=None):
    if input_data is None:
        return []

    # Parse input JSON data
    try:
        data = json.loads(input_data)
        recipient_email = data.get('recipient')
        names = data.get('names', [])
    except (json.JSONDecodeError, ValueError):
        return []

    if not recipient_email or not names:
        return []

    message = 'Subject: Extracted Names\n\n' + '\n'.join(names)
    
    if smtp:
        server = smtp(smtp_server, smtp_port)
    else:
        server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(email_address, email_password)
    server.sendmail(email_address, recipient_email, message)
    server.quit()
    return names

def test_task_func():
    # Test case 1: input_data is None
    assert task_func(input_data=None) == []

    # Test case 2: input_data is not a valid JSON string
    assert task_func(input_data='invalid_json_string') == []

    # Test case 3: input_data is a valid JSON string but missing 'recipient' key
    assert task_func(input_data='{"names": ["John", "Jane"]}') == []

    # Test case 4: input_data is a valid JSON string but missing 'names' key
    assert task_func(input_data='{"recipient": "john.doe@example.com"}') == []

    # Test case 5: input_data is a valid JSON string with valid data
    assert task_func(input_data='{"recipient": "john.doe@example.com", "names": ["John", "Jane"]}') == ["John", "Jane"]

    # Test case 6: input_data is a valid JSON string with valid data and custom smtp object
    class CustomSMTP:
        def __init__(self, server, port):
            self.server = server
            self.port = port
        def sendmail(self, sender, recipient, message):
            pass

    assert task_func(input_data='{"recipient": "john.doe@example.com", "names": ["John", "Jane"]}', smtp=CustomSMTP('custom_smtp.com', 587)) == ["John", "Jane"]