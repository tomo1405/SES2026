import pytest
from unittest.mock import patch, MagicMock
from src_1043 import task_func

@patch('src_1043.getpass.getpass')
@patch('src_1043.smtplib.SMTP')
def test_task_func(mock_smtp, mock_getpass):
    # Mocking the input values for getpass
    mock_getpass.side_effect = ["test@example.com", "recipient@example.com", "password"]

    # Mocking the client socket
    client_socket = MagicMock()
    client_socket.recv.return_value = b"Hello, this is a test message."
    
    # Call the function
    task_func(client_socket)

    # Assertions
    client_socket.recv.assert_called_once_with(1024)
    client_socket.send.assert_called_once_with(b"Message sent.")
    client_socket.close.assert_called_once()

    # Check if SMTP was used correctly
    mock_smtp.assert_called_once_with("smtp.gmail.com", 587)
    smtp_instance = mock_smtp.return_value
    smtp_instance.starttls.assert_called_once()
    smtp_instance.login.assert_called_once_with("test@example.com", "password")
    smtp_instance.send_message.assert_called_once()

    # Check if EmailMessage was set up correctly
    email = EmailMessage()
    email["From"] = "test@example.com"
    email["To"] = "recipient@example.com"
    email["Subject"] = "Message from socket client"
    email.set_content("Hello, this is a test message.")
    assert email == smtp_instance.send_message.call_args[0][0]