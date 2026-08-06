import json
import requests
import pytest
from src_1134 import task_func

def test_task_func():
    API_URL = "https://api.example.com/"
    endpoint = "users"
    PREFIX = "data/"

    with pytest.raises(RuntimeError) as exc_info:
        task_func(API_URL, endpoint, PREFIX)

    assert "Error fetching data from API" in str(exc_info.value)

def test_task_func_with_valid_response():
    API_URL = "https://api.example.com/"
    endpoint = "users"
    PREFIX = "data/"
    response_data = {"name": "John Doe", "age": 30}
    response = requests.Response()
    response._content = json.dumps(response_data).encode('utf-8')

    filename = task_func(API_URL, endpoint, PREFIX)

    assert filename == f"{PREFIX}{endpoint}.json"