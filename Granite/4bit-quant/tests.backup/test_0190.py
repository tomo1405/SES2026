import re
import json
import requests
import pytest

def task_func(data_url: str) -> list:
    try:
        response = requests.get(data_url)
        data = response.json()
        data_string = json.dumps(data['names'])
        names = re.findall(r'(?<!\[)(\w+)(?![\w]*\])', data_string)
        return names
    except Exception as e:
        return "Invalid url input"

def test_task_func():
    data_url = "https://jsonplaceholder.typicode.com/users"
    expected_output = ["typicode", "msn", "jsonplaceholder"]
    actual_output = task_func(data_url)
    assert actual_output == expected_output, "Output does not match expected output"

def test_task_func_invalid_url():
    data_url = "invalid_url"
    expected_output = "Invalid url input"
    actual_output = task_func(data_url)
    assert actual_output == expected_output, "Output does not match expected output"