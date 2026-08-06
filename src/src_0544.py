import base64
import os
def task_func():
    float_bytes = os.urandom(4)
    encoded_str = base64.b64encode(float_bytes)

    return encoded_str.decode()