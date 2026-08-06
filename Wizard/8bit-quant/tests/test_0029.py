python
import pytest
import requests
import json
import base64
from src_0029 import task_func

def test_task_func():
    data = {"key1": "value1", "key2": "value2"}
    response = task_func(data)
    assert response.status_code == 200
    assert response.json()["status"] == "success"