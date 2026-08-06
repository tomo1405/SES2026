import pytest
from unittest.mock import patch, Mock
from src_0275 import task_func

def test_do_POST_json_content_type():
    handler = task_func('smtp.example.com', 587, 'user@example.com', 'password')()
    handler.wfile = Mock()
    handler.rfile = Mock()
    handler.headers = {'content-type': 'application/json'}
    handler.rfile.read.return_value = b'{"subject": "Test", "message": "Hello", "to": "test@example.com"}'

    handler.do_POST()

    handler.send_response.assert_called_once_with(200)
    handler.end_headers.assert_called_once()

def test_do_POST_invalid_json():
    handler = task_func('smtp.example.com', 587, 'user@example.com', 'password')()
    handler.wfile = Mock()
    handler.rfile = Mock()
    handler.headers = {'content-type': 'application/json'}
    handler.rfile.read.return_value = b'invalid json'

    handler.do_POST()

    handler.send_response.assert_called_once_with(400)
    handler.end_headers.assert_called_once()

def test_do_POST_missing_fields():
    handler = task_func('smtp.example.com', 587, 'user@example.com', 'password')()
    handler.wfile = Mock()
    handler.rfile = Mock()
    handler.headers = {'content-type': 'application/json'}
    handler.rfile.read.return_value = b'{"subject": "Test", "message": "Hello"}'

    handler.do_POST()

    handler.send_response.assert_called_once_with(400)
    handler.end_headers.assert_called_once()

def test_do_POST_smtp_authentication_error():
    handler = task_func('smtp.example.com', 587, 'user@example.com', 'password')()
    handler.wfile = Mock()
    handler.rfile = Mock()
    handler.headers = {'content-type': 'application/json'}
    handler.rfile.read.return_value = b'{"subject": "Test", "message": "Hello", "to": "test@example.com"}'

    with patch('smtplib.SMTP') as mock_smtp:
        mock_smtp.return_value.starttls = Mock()
        mock_smtp.return_value.login = Mock(side_effect=smtplib.SMTPAuthenticationError)
        handler.do_POST()

    handler.send_response.assert_called_once_with(535)
    handler.end_headers.assert_called_once()

def test_do_POST_non_json_content_type():
    handler = task_func('smtp.example.com', 587, 'user@example.com', 'password')()
    handler.wfile = Mock()
    handler.rfile = Mock()
    handler.headers = {'content-type': 'text/plain'}

    handler.do_POST()

    handler.send_response.assert_called_once_with(400)
    handler.end_headers.assert_called_once()