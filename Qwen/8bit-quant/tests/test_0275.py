import pytest
from unittest.mock import patch, Mock
from src_0275 import task_func

class TestEmailRequestHandler:
    @patch('src_0275.smtplib.SMTP')
    @patch('src_0275.json.loads')
    @patch('src_0275.cgi.parse_header')
    def test_do_POST_success(self, mock_parse_header, mock_json_loads, mock_smtp):
        # Arrange
        handler = task_func("smtp.example.com", 587, "user@example.com", "password")()
        handler.wfile = Mock()
        handler.headers = {
            'content-type': 'application/json',
            'content-length': '50'
        }
        mock_parse_header.return_value = ('application/json', {})
        mock_json_loads.return_value = {
            'subject': 'Test Subject',
            'message': 'Test Message',
            'to': 'recipient@example.com'
        }
        mock_smtp_instance = Mock()
        mock_smtp.return_value = mock_smtp_instance
        mock_smtp_instance.starttls = Mock()
        mock_smtp_instance.login = Mock()
        mock_smtp_instance.sendmail = Mock()

        # Act
        handler.do_POST()

        # Assert
        mock_parse_header.assert_called_once_with(handler.headers.get('content-type'))
        mock_json_loads.assert_called_once_with(b'{"subject": "Test Subject", "message": "Test Message", "to": "recipient@example.com"}')
        mock_smtp.assert_called_once_with("smtp.example.com", 587)
        mock_smtp_instance.starttls.assert_called_once()
        mock_smtp_instance.login.assert_called_once_with("user@example.com", "password")
        mock_smtp_instance.sendmail.assert_called_once_with("user@example.com", ["recipient@example.com"], mock.ANY)
        handler.wfile.write.assert_called_once_with(b'HTTP/1.0 200 OK\r\n\r\n')

    @patch('src_0275.cgi.parse_header')
    def test_do_POST_invalid_content_type(self, mock_parse_header):
        # Arrange
        handler = task_func("smtp.example.com", 587, "user@example.com", "password")()
        handler.wfile = Mock()
        handler.headers = {
            'content-type': 'text/plain',
            'content-length': '50'
        }
        mock_parse_header.return_value = ('text/plain', {})

        # Act
        handler.do_POST()

        # Assert
        mock_parse_header.assert_called_once_with(handler.headers.get('content-type'))
        handler.wfile.write.assert_called_once_with(b'HTTP/1.0 400 Bad Request\r\n\r\n')

    @patch('src_0275.json.loads')
    @patch('src_0275.cgi.parse_header')
    def test_do_POST_json_decode_error(self, mock_parse_header, mock_json_loads):
        # Arrange
        handler = task_func("smtp.example.com", 587, "user@example.com", "password")()
        handler.wfile = Mock()
        handler.headers = {
            'content-type': 'application/json',
            'content-length': '50'
        }
        mock_parse_header.return_value = ('application/json', {})
        mock_json_loads.side_effect = json.JSONDecodeError("Expecting value", "", 0)

        # Act
        handler.do_POST()

        # Assert
        mock_parse_header.assert_called_once_with(handler.headers.get('content-type'))
        mock_json_loads.assert_called_once_with(b'{"subject": "Test Subject", "message": "Test Message", "to": "recipient@example.com"}')
        handler.wfile.write.assert_called_once_with(b'HTTP/1.0 400 Bad Request\r\n\r\n')

    @patch('src_0275.json.loads')
    @patch('src_0275.cgi.parse_header')
    def test_do_POST_missing_fields(self, mock_parse_header, mock_json_loads):
        # Arrange
        handler = task_func("smtp.example.com", 587, "user@example.com", "password")()
        handler.wfile = Mock()
        handler.headers = {
            'content-type': 'application/json',
            'content-length': '50'
        }
        mock_parse_header.return_value = ('application/json', {})
        mock_json_loads.return_value = {
            'subject': 'Test Subject',
            'message': 'Test Message'
        }

        # Act
        handler.do_POST()

        # Assert
        mock_parse_header.assert_called_once_with(handler.headers.get('content-type'))
        mock_json_loads.assert_called_once_with(b'{"subject": "Test Subject", "message": "Test Message"}')
        handler.wfile.write.assert_called_once_with(b'HTTP/1.0 400 Bad Request\r\n\r\n')

    @patch('src_0275.smtplib.SMTP')
    @patch('src_0275.json.loads')
    @patch('src_0275.cgi.parse_header')
    def test_do_POST_smtp_authentication_error(self, mock_parse_header, mock_json_loads, mock_smtp):
        # Arrange
        handler = task_func("smtp.example.com", 587, "user@example.com", "password")()
        handler.wfile = Mock()
        handler.headers = {
            'content-type': 'application/json',
            'content-length': '50'
        }
        mock_parse_header.return_value = ('application/json', {})
        mock_json_loads.return_value = {
            'subject': 'Test Subject',
            'message': 'Test Message',
            'to': 'recipient@example.com'
        }
        mock_smtp_instance = Mock()
        mock_smtp.return_value = mock_smtp_instance
        mock_smtp_instance.starttls = Mock()
        mock_smtp_instance.login = Mock(side_effect=smtplib.SMTPAuthenticationError)
        mock_smtp_instance.sendmail = Mock()

        # Act
        handler.do_POST()

        # Assert
        mock_parse_header.assert_called_once_with(handler.headers.get('content-type'))
        mock_json_loads.assert_called_once_with(b'{"subject": "Test Subject", "message": "Test Message", "to": "recipient@example.com"}')
        mock_smtp.assert_called_once_with("smtp.example.com", 587)
        mock_smtp_instance.starttls.assert_called_once()
        mock_smtp_instance.login.assert_called_once_with("user@example.com", "password")
        handler.wfile.write.assert_called_once_with(b'HTTP/1.0 535 Authentication Failed\r\n\r\n')