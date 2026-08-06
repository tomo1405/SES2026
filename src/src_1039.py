from datetime import datetime
import json
SERVER_ADDRESS = "localhost"
BUFFER_SIZE = 1024
def task_func(client_socket):
    response_data = {"message": "Hello", "time": str(datetime.now())}
    response = json.dumps(response_data) + "\n"
    client_socket.send(response.encode("utf-8"))
    client_socket.close()