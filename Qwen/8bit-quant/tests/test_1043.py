from unittest.mock import Mock, call, patch

import pytest
from src_1043 import task_func


@pytest.fixture
def mock_socket():
    mock_socket = Mock()
    mock_socket.recv.return_value = b"Test message"
    return mock_socket

@patch('src_1043.getpass.getpass')
@patch('src_1043.smtplib.SMTP')
def test_task_func(mock_smtp, mock_getpass, mock_socket):
    # Mock user inputs
    mock_getpass.side_effect = ["sender@example.com", "recipient@example.com", "password"]

    # Call the function
    task_func(mock_socket)

    # Assertions
    mock_socket.recv.assert_called_once_with(1024)
    mock_getpass.assert_has_calls([
        call("Email: "),
        call("Recipient: "),
        call("Password: ")
    ])

    # Check SMTP interactions
    mock_smtp.assert_called_once_with("smtp.gmail.com", 587)
    smtp_instance = mock_smtp.return_value
    smtp_instance.starttls.assert_called_once()
    smtp_instance.login.assert_called_once_with("sender@example.com", "password")
    smtp_instance.send_message.assert_called_once()

    # Check socket response
    mock_socket.send.assert_called_once_with(b"Message sent.")
    mock_socket.close.assert_called_once()