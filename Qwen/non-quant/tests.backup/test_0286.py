import pytest
from src_0286 import task_func

# Mocking the mechanize and BeautifulSoup libraries for testing
class MockResponse:
    def __init__(self, content):
        self.content = content

    def read(self):
        return self.content

class MockBrowser:
    def open(self, url):
        pass

    def select_form(self, nr):
        pass

    def __setitem__(self, key, value):
        pass

    def submit(self):
        return MockResponse(b"<html><head><title>Test Title</title></head><body></body></html>")

class MockBeautifulSoup:
    def __init__(self, markup, parser):
        self.title = MockTag("Test Title")

class MockTag:
    def __init__(self, string):
        self.string = string

@pytest.fixture
def mock_mechanize(monkeypatch):
    monkeypatch.setattr('src_0286.mechanize.Browser', MockBrowser)
    monkeypatch.setattr('src_0286.BeautifulSoup', MockBeautifulSoup)

def test_task_func(mock_mechanize):
    url = "http://example.com"
    form_id = 0
    data = {"field1": "value1", "field2": "value2"}
    result = task_func(url, form_id, data)
    assert result == "Test Title"