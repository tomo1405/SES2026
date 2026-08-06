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
    # Test case 1: Valid input data
    input_data = '{"recipient": "recipient@email.com", "names": ["John", "Jane", "Bob"]}'
    assert task_func(input_data) == ["John", "Jane", "Bob"]

    # Test case 2: Invalid input data (missing recipient email)
    input_data = '{"names": ["John", "Jane", "Bob"]}'
    assert task_func(input_data) == []

    # Test case 3: Invalid input data (missing names)
    input_data = '{"recipient": "recipient@email.com"}'
    assert task_func(input_data) == []

    # Test case 4: Invalid input data (invalid JSON)
    input_data = '{"recipient": "recipient@email.com", "names": ["John", "Jane", "Bob"'
    assert task_func(input_data) == []

    # Test case 5: Invalid input data (invalid SMTP server)
    input_data = '{"recipient": "recipient@email.com", "names": ["John", "Jane", "Bob"]}'
    assert task_func(input_data, smtp_server="invalid.smtp.server.com") == []

    # Test case 6: Invalid input data (invalid SMTP port)
    input_data = '{"recipient": "recipient@email.com", "names": ["John", "Jane", "Bob"]}'
    assert task_func(input_data, smtp_port=1234) == []

    # Test case 7: Invalid input data (invalid email address)
    input_data = '{"recipient": "recipient@email.com", "names": ["John", "Jane", "Bob"]}'
    assert task_func(input_data, email_address="invalid.email@gmail.com") == []

    # Test case 8: Invalid input data (invalid email password)
    input_data = '{"recipient": "recipient@email.com", "names": ["John", "Jane", "Bob"]}'
    assert task_func(input_data, email_password="invalid.password") == []

    # Test case 9: Invalid input data (invalid SMTP object)
    input_data = '{"recipient": "recipient@email.com", "names": ["John", "Jane", "Bob"]}'
    assert task_func(input_data, smtp=1234) == []