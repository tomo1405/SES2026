import json
import re

import requests
from src_0190 import task_func


def test_task_func():
    data_url = "https://api.example.com/data"
    expected_names = ["John", "Jane", "Jim"]

    response = requests.get(data_url)
    data = response.json()
    data_string = json.dumps(data['names'])
    names = re.findall(r'(?<!\[)(\w+)(?![\w]*\])', data_string)

    assert names == expected_names

def test_task_func_invalid_url():
    data_url = "invalid_url"
    expected_result = "Invalid url input"

    result = task_func(data_url)

    assert result == expected_result