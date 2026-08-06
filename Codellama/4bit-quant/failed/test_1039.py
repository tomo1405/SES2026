import pytest
from src_1039 import task_func

def test_task_func():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_ADDRESS, BUFFER_SIZE))
    task_func(client_socket)
    response = client_socket.recv(BUFFER_SIZE).decode("utf-8")
    response_data = json.loads(response)
    assert response_data["message"] == "Hello"
    assert response_data["time"] == str(datetime.now())
    client_socket.close()