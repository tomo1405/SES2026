import pytest
from src_1019 import task_func
from bs4 import BeautifulSoup
import requests

# Mocking the requests module
class MockResponse:
    def __init__(self, content, status_code):
        self.content = content
        self.status_code = status_code

    def raise_for_status(self):
        if self.status_code != 200:
            raise requests.exceptions.HTTPError(f"HTTP Error {self.status_code}")

def mock_requests_get(url, timeout=None):
    if url == "http://example.com":
        return MockResponse(b"<html><body><h1>Test</h1></body></html>", 200)
    elif url == "http://error.com":
        return MockResponse(b"", 404)
    else:
        return MockResponse(b"", 500)

@pytest.fixture
def mock_requests(monkeypatch):
    monkeypatch.setattr(requests, 'get', mock_requests_get)

def test_task_func_success(mock_requests):
    result = task_func("http://example.com")
    assert isinstance(result, BeautifulSoup)
    assert result.prettify() == "<html><body><h1>Test</h1></body></html>"

def test_task_func_failure(mock_requests):
    result = task_func("http://error.com")
    assert result is None

def test_task_func_empty_url():
    result = task_func("")
    assert result is None

def test_task_func_invalid_url(mock_requests):
    result = task_func("http://invalid.com")
    assert result is None

def test_task_func_with_lxml_parser(mock_requests):
    result = task_func("http://example.com", use_lxml=True)
    assert isinstance(result, BeautifulSoup)
    assert result.prettify() == "<html><body><h1>Test</h1></body></html>"

def test_task_func_with_html_parser(mock_requests):
    result = task_func("http://example.com", use_lxml=False)
    assert isinstance(result, BeautifulSoup)
    assert result.prettify() == "<html><body><h1>Test</h1></body></html>"