import pytest
from src_0029 import task_func

def test_task_func():
    data = {"key1": "value1", "key2": "value2"}
    url = "http://your-api-url.com"
    response = task_func(data, url)
    assert response.status_code == 200
    assert response.json()["payload"] == base64.b64encode(json.dumps(data).encode('ascii')).decode('ascii')