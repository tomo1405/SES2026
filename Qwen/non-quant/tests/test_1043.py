import getpass
import smtplib
from unittest.mock import patch

import pytest
from src_1043 import task_func


@pytest.fixture
def mock_client_socket():
    class MockSocket:
        def __init__(self):
            self.sent_data = None

        def recv(self, size):
            return b"Test message"

        def send(self, data):
            self.sent_data = data

        def close(self):
            pass

    return MockSocket()

@pytest.fixture
def mock_getpass(monkeypatch):
    monkeypatch.setattr(getpass, 'getpass', lambda prompt: "test@example.com")

@pytest.fixture
def mock_smtplib_send_message(monkeypatch):
    def mock_send_message(smtp, email):
        pass
    monkeypatch.setattr(smtplib.SMTP, 'send_message', mock_send_message)

def test_task_func(mock_client_socket, mock_getpass, mock_smtplib_send_message):
    task_func(mock_client_socket)
    assert mock_client_socket.sent_data == b"Message sent."

@patch('src_1043.EmailMessage')
@patch('src_1043.smtplib.SMTP')
def test_task_func_email_creation(mock_smtp, mock_email, mock_client_socket, mock_getpass):
    task_func(mock_client_socket)
    mock_email.assert_called_once()
    email_instance = mock_email.return_value
    assert email_instance["From"] == "test@example.com"
    assert email_instance["To"] == "test@example.com"
    assert email_instance["Subject"] == "Message from socket client"
    assert email_instance.get_content() == "Test message"

@patch('src_1043.smtplib.SMTP')
def test_task_func_smtp_login(mock_smtp, mock_client_socket, mock_getpass):
    task_func(mock_client_socket)
    mock_smtp.assert_called_once_with("smtp.gmail.com", 587)
    smtp_instance = mock_smtp.return_value
    smtp_instance.starttls.assert_called_once()
    smtp_instance.login.assert_called_once_with("test@example.com", "test@example.com")

@patch('src_1043.getpass.getpass')
def test_task_func_password_prompt(mock_getpass, mock_client_socket):
    mock_getpass.side_effect = ["test@example.com", "recipient@example.com", "password123"]
    task_func(mock_client_socket)
    assert mock_getpass.call_count == 3
    calls = mock_getpass.call_args_list
    assert calls[0][0] == ("Email: ",)
    assert calls[1][0] == ("Recipient: ",)
    assert calls[2][0] == ("Password: ",)