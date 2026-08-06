import getpass
from unittest.mock import Mock, patch

from src_1043 import task_func


def test_task_func():
    # Mock the client socket
    client_socket = Mock()

    # Test if the function prints the correct message when it receives a request
    request = "Hello, world!"
    client_socket.recv.return_value = request.encode("utf-8")
    task_func(client_socket)
    client_socket.recv.assert_called_once_with(1024)
    print.assert_called_once_with(f"Received: {request}")

    # Test if the function sends the correct email when it receives a request
    email_from = "sender@example.com"
    email_to = "recipient@example.com"
    email_password = "password"
    client_socket.recv.return_value = request.encode("utf-8")
    getpass.getpass.side_effect = [email_from, email_to, email_password]
    with patch("smtplib.SMTP") as mock_smtp:
        task_func(client_socket)
        mock_smtp.assert_called_once_with("smtp.gmail.com", 587)
        mock_smtp.return_value.starttls.assert_called_once()
        mock_smtp.return_value.login.assert_called_once_with(email_from, email_password)
        mock_smtp.return_value.send_message.assert_called_once()