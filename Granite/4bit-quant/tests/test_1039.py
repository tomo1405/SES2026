import json
from datetime import datetime
from unittest.mock import Mock

from src_1039 import task_func


def test_task_func():
    client_socket = Mock()  # Create a mock client socket
    task_func(client_socket)  # Call the function with the mock socket
    response_data = {"message": "Hello", "time": str(datetime.now())}
    response = json.dumps(response_data) + "\n"
    client_socket.send.assert_called_with(response.encode("utf-8"))  # Assert that the socket's send method was called with the correct argument
    client_socket.close.assert_called_once()  # Assert that the socket's close method was called exactly once