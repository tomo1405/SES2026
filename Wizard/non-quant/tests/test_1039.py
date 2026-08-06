python
import pytest
from src_1039 import task_func

def test_task_func():
    client_socket = "client_socket"
    response_data = {"message": "Hello", "time": str(datetime.now())}
    response = json.dumps(response_data) + "\n"
    with pytest.raises(AttributeError):
        task_func(client_socket)