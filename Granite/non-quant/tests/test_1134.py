import json
import requests
import pytest
from src_1134 import task_func

def test_task_func():
    API_URL = "https://api.example.com/"
    endpoint = "users"
    PREFIX = "data/"

    filename = task_func(API_URL, endpoint, PREFIX)

    assert filename.startswith(PREFIX)
    assert filename.endswith(f".json")

    with open(filename, 'r') as f:
        data = json.load(f)

    assert isinstance(data, list)
    assert len(data) > 0