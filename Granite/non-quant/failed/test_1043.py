import pytest
from src_1043 import task_func

def test_task_func():
    client_socket = Mock()
    request = "This is a test message."
    client_socket.recv.return_value = request.encode("utf-8")
    email_from = "test@example.com"
    email_to = "recipient@example.com"
    password = "password123"
    with patch("getpass.getpass") as mock_getpass:
        mock_getpass.side_effect = [email_from, email_to, password]
        task_func(client_socket)
    email = client_socket.send.call_args[0][0]
    assert email["From"] == email_from
    assert email["To"] == email_to
    assert email["Subject"] == "Message from socket client"
    assert email.get_content() == request
    assert client_socket.send.call_args[0][0].encode("utf-8") == b"Message sent."