import json
from datetime import datetime
from unittest.mock import Mock

from src_1039 import task_func


def test_task_func():
    client_socket = Mock()  # You can use a mock object for testing purposes
    response_data = {"message": "Hello", "time": str(datetime.now())}
    response = json.dumps(response_data) + "\n"
    task_func(client_socket)
    client_socket.send.assert_called_with(response.encode("utf-8"))
    client_socket.close.assert_called_once()