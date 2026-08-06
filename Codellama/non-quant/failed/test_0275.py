import pytest
from src_0275 import task_func

def test_task_func():
    smtp_server = 'smtp.example.com'
    smtp_port = 587
    smtp_username = 'user@example.com'
    smtp_password = 'password'

    handler = task_func(smtp_server, smtp_port, smtp_username, smtp_password)

    # Test with valid JSON data
    data = {'subject': 'Test Subject', 'message': 'Test Message', 'to': 'recipient@example.com'}
    handler.do_POST(data)
    assert handler.wfile.getvalue() == b'200 OK'

    # Test with invalid JSON data
    data = {'subject': 'Test Subject', 'message': 'Test Message', 'to': 'recipient@example.com'}
    handler.do_POST(data)
    assert handler.wfile.getvalue() == b'400 Bad Request'

    # Test with missing required fields
    data = {'subject': 'Test Subject', 'message': 'Test Message'}
    handler.do_POST(data)
    assert handler.wfile.getvalue() == b'400 Bad Request'

    # Test with invalid email address
    data = {'subject': 'Test Subject', 'message': 'Test Message', 'to': 'invalid_email'}
    handler.do_POST(data)
    assert handler.wfile.getvalue() == b'400 Bad Request'

    # Test with invalid SMTP server
    data = {'subject': 'Test Subject', 'message': 'Test Message', 'to': 'recipient@example.com'}
    handler.do_POST(data)
    assert handler.wfile.getvalue() == b'535 Authentication failed'