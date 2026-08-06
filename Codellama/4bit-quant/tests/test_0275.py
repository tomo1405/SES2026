import io

from src_0275 import task_func


def test_task_func():
    smtp_server = 'smtp.example.com'
    smtp_port = 587
    smtp_username = 'username'
    smtp_password = 'password'
    email_data = {'subject': 'Test Email', 'message': 'This is a test email', 'to': 'recipient@example.com'}

    handler = task_func(smtp_server, smtp_port, smtp_username, smtp_password)
    handler.do_POST()

    assert handler.wfile.getvalue() == b'{"status": "success"}'

def test_task_func_invalid_json():
    smtp_server = 'smtp.example.com'
    smtp_port = 587
    smtp_username = 'username'
    smtp_password = 'password'
    email_data = {'subject': 'Test Email', 'message': 'This is a test email', 'to': 'recipient@example.com'}

    handler = task_func(smtp_server, smtp_port, smtp_username, smtp_password)
    handler.headers = {'content-type': 'application/json'}
    handler.rfile = io.BytesIO(b'{"subject": "Test Email", "message": "This is a test email", "to": "recipient@example.com"}')
    handler.do_POST()

    assert handler.wfile.getvalue() == b'{"status": "error", "message": "Invalid JSON data"}'

def test_task_func_missing_fields():
    smtp_server = 'smtp.example.com'
    smtp_port = 587
    smtp_username = 'username'
    smtp_password = 'password'
    email_data = {'subject': 'Test Email', 'message': 'This is a test email', 'to': 'recipient@example.com'}

    handler = task_func(smtp_server, smtp_port, smtp_username, smtp_password)
    handler.headers = {'content-type': 'application/json'}
    handler.rfile = io.BytesIO(b'{"subject": "Test Email", "message": "This is a test email"}')
    handler.do_POST()

    assert handler.wfile.getvalue() == b'{"status": "error", "message": "Missing fields"}'

def test_task_func_invalid_smtp_credentials():
    smtp_server = 'smtp.example.com'
    smtp_port = 587
    smtp_username = 'username'
    smtp_password = 'password'
    email_data = {'subject': 'Test Email', 'message': 'This is a test email', 'to': 'recipient@example.com'}

    handler = task_func(smtp_server, smtp_port, smtp_username, smtp_password)
    handler.headers = {'content-type': 'application/json'}
    handler.rfile = io.BytesIO(b'{"subject": "Test Email", "message": "This is a test email", "to": "recipient@example.com"}')
    handler.do_POST()

    assert handler.wfile.getvalue() == b'{"status": "error", "message": "Invalid SMTP credentials"}'