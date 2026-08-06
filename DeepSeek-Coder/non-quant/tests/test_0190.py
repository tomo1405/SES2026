import pytest
from src_0190 import task_func

def test_task_func_valid_input():
    url = "https://example.com/api"
    response_mock = {
        "names": ["John Doe", "Jane Smith"]
    }
    with requests_mock.Mocker() as mocker:
        mocker.get(url, json=response_mock)
        result = task_func(url)
        assert result == ["John Doe", "Jane Smith"]

def test_task_func_invalid_input():
    url = "invalid_url"
    result = task_func(url)
    assert result == "Invalid url input"