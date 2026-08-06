import base64
import json
import zlib
def task_func(data_dict):
    json_str = json.dumps(data_dict)
    compressed = zlib.compress(json_str.encode())
    return base64.b64encode(compressed).decode()