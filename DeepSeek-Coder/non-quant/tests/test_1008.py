import pytest
from src_1008 import task_func
import requests
import pandas as pd

@pytest.fixture
def mock_response():
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

        def raise_for_status(self):
            if self.status_code != 200:
                raise requests.HTTPError("Mock HTTPError")

    return MockResponse({"key": "value"}, 200)

@pytest.fixture
def mock_response_error():
    class MockResponseError:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

        def raise_for_status(self):
            raise requests.HTTPError("Mock HTTPError")

    return MockResponseError({"key": "value"}, 500)

def test_task_func_success(monkeypatch):
    monkeypatch.setattr(requests, 'get', mock_response)
    result = task_func("http://example.com")
    assert isinstance(result, pd.DataFrame)

def test_task_func_error(monkeypatch):
    monkeypatch.setattr(requests, 'get', mock_response_error)
    with pytest.raises(SystemError):
        task_func("http://example.com")

def test_task_func_invalid_json(monkeypatch):
    monkeypatch.setattr(requests, 'get', mock_response)
    with pytest.raises(ValueError):
        task_func("http://example.com")