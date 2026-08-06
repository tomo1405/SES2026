import pytest
from src_0285 import task_func
from unittest.mock import patch
from bs4 import BeautifulSoup

@pytest.fixture
def mock_browser():
    class MockResponse:
        def read(self):
            return b'<html><body><a href="/page1">Page 1</a><a href="https://external.com/page2">Page 2</a></body></html>'

    class MockBrowser:
        def open(self, url):
            return MockResponse()

    return MockBrowser()

@patch('src_0285.mechanize.Browser', return_value=mock_browser())
def test_task_func(mock_browser):
    url = 'http://example.com'
    expected_links = [
        'http://example.com/page1',
        'https://external.com/page2'
    ]
    assert task_func(url) == expected_links