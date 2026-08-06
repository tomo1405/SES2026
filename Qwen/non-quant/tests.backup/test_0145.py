import pytest
from src_0145 import task_func
import ipaddress
import requests

# Mocking the requests module to simulate responses
class MockResponse:
    def __init__(self, status_code):
        self.status_code = status_code

class MockRequests:
    def get(self, url, timeout):
        # Simulate a successful response for a specific IP
        if url == "http://192.168.1.1":
            return MockResponse(200)
        # Simulate a connection error for another IP
        elif url == "http://192.168.1.2":
            raise requests.exceptions.ConnectionError("Connection refused")
        else:
            return MockResponse(404)

@pytest.fixture
def mock_requests(monkeypatch):
    monkeypatch.setattr(requests, 'get', MockRequests().get)

def test_task_func_valid_ip_range(mock_requests):
    ip_range = "192.168.1.0/30"
    timeout = 5
    expected_result = ["192.168.1.1"]
    assert task_func(ip_range, timeout) == expected_result

def test_task_func_invalid_ip_range():
    ip_range = "invalid_ip_range"
    timeout = 5
    with pytest.raises(ValueError, match="Invalid IP range"):
        task_func(ip_range, timeout)

def test_task_func_connection_error(mock_requests):
    ip_range = "192.168.1.0/31"
    timeout = 5
    expected_result = []
    assert task_func(ip_range, timeout) == expected_result

def test_task_func_no_successful_connections(mock_requests):
    ip_range = "192.168.1.2/31"
    timeout = 5
    expected_result = []
    assert task_func(ip_range, timeout) == expected_result