import pytest
from src_0026 import task_func
import base64
import json
import zlib

def test_task_func():
    data_dict = {"key": "value"}
    expected_output = base64.b64encode(zlib.compress(json.dumps(data_dict).encode())).decode()
    assert task_func(data_dict) == expected_output