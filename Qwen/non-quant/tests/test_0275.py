import pytest
from unittest.mock import patch, Mock
from src_0275 import task_func

class TestEmailRequestHandler:
    @patch('smtplib.SMTP')
    def test_do_POST_valid_json_and_email_sent(self, mock_smtp):
        # Arrange
        smtp_server = 'smtp.example.com'
        smtp_port = 587
        smtp_username = 'user@example.com'
        smtp_password = 'password'
        request_handler_class = task_func(smtp_server, smtp_port, smtp_username, smtp_password)
        request_handler = request_handler_class(Mock(), Mock())
        request_handler.headers = {
            'content-type': 'application/json',
            'content-length': '61'
        }
        request_handler.rfile.read.return_value = b'{"subject": "Test", "message": "Hello", "to": "recipient@example.com"}'

        # Act
        request_handler.do_POST()

        # Assert
        mock_smtp.assert_called_once_with(smtp_server, smtp_port)
        mock_smtp_instance = mock_smtp.return_value
        mock_smtp_instance.starttls.assert_called_once()
        mock_smtp_instance.login.assert_called_once_with(smtp_username, smtp_password)
        mock_smtp_instance.sendmail.assert_called_once_with(smtp_username, ['recipient@example.com'], 'Content-Type: text/plain; charset="us-ascii"\nMIME-Version: 1.0\nContent-Transfer-Encoding: 7bit\nSubject: Test\nFrom: user@example.com\nTo: recipient@example.com\n\nHello')
        request_handler.wfile.write.assert_called_once_with(b'')

    @patch('smtplib.SMTP')
    def test_do_POST_invalid_json(self, mock_smtp):
        # Arrange
        smtp_server = 'smtp.example.com'
        smtp_port = 587
        smtp_username = 'user@example.com'
        smtp_password = 'password'
        request_handler_class = task_func(smtp_server, smtp_port, smtp_username, smtp_password)
        request_handler = request_handler_class(Mock(), Mock())
        request_handler.headers = {
            'content-type': 'application/json',
            'content-length': '10'
        }
        request_handler.rfile.read.return_value = b'invalid json'

        # Act
        request_handler.do_POST()

        # Assert
        mock_smtp.assert_not_called()
        request_handler.send_response.assert_called_once_with(400)
        request_handler.end_headers.assert_called_once()

    @patch('smtplib.SMTP')
    def test_do_POST_missing_fields(self, mock_smtp):
        # Arrange
        smtp_server = 'smtp.example.com'
        smtp_port = 587
        smtp_username = 'user@example.com'
        smtp_password = 'password'
        request_handler_class = task_func(smtp_server, smtp_port, smtp_username, smtp_password)
        request_handler = request_handler_class(Mock(), Mock())
        request_handler.headers = {
            'content-type': 'application/json',
            'content-length': '41'
        }
        request_handler.rfile.read.return_value = b'{"subject": "Test", "message": "Hello"}'

        # Act
        request_handler.do_POST()

        # Assert
        mock_smtp.assert_not_called()
        request_handler.send_response.assert_called_once_with(400)
        request_handler.end_headers.assert_called_once()

    @patch('smtplib.SMTP')
    def test_do_POST_invalid_content_type(self, mock_smtp):
        # Arrange
        smtp_server = 'smtp.example.com'
        smtp_port = 587
        smtp_username = 'user@example.com'
        smtp_password = 'password'
        request_handler_class = task_func(smtp_server, smtp_port, smtp_username, smtp_password)
        request_handler = request_handler_class(Mock(), Mock())
        request_handler.headers = {
            'content-type': 'text/plain',
            'content-length': '41'
        }
        request_handler.rfile.read.return_value = b'{"subject": "Test", "message": "Hello", "to": "recipient@example.com"}'

        # Act
        request_handler.do_POST()

        # Assert
        mock_smtp.assert_not_called()
        request_handler.send_response.assert_called_once_with(400)
        request_handler.end_headers.assert_called_once()

    @patch('smtplib.SMTP')
    def test_do_POST_smtp_authentication_error(self, mock_smtp):
        # Arrange
        smtp_server = 'smtp.example.com'
        smtp_port = 587
        smtp_username = 'user@example.com'
        smtp_password = 'password'
        request_handler_class = task_func(smtp_server, smtp_port, smtp_username, smtp_password)
        request_handler = request_handler_class(Mock(), Mock())
        request_handler.headers = {
            'content-type': 'application/json',
            'content-length': '61'
        }
        request_handler.rfile.read.return_value = b'{"subject": "Test", "message": "Hello", "to": "recipient@example.com"}'
        mock_smtp_instance = mock_smtp.return_value
        mock_smtp_instance.login.side_effect = smtplib.SMTPAuthenticationError

        # Act
        request_handler.do_POST()

        # Assert
        mock_smtp.assert_called_once_with(smtp_server, smtp_port)
        mock_smtp_instance.starttls.assert_called_once()
        mock_smtp_instance.login.assert_called_once_with(smtp_username, smtp_password)
        mock_smtp_instance.sendmail.assert_not_called()
        request_handler.send_response.assert_called_once_with(535)
        request_handler.end_headers.assert_called_once()