python
import pytest
from src_1039 import task_func

def test_task_func():
    client_socket = "client_socket"
    response_data = {"message": "Hello", "time": str(datetime.now())}
    response = json.dumps(response_data) + "\n"
    task_func(client_socket)
    assert client_socket.send.call_args[0][0].decode("utf-8") == response