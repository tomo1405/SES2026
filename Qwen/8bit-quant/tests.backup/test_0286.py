import pytest
from src_0286 import task_func

# Mocking dependencies
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
        return MockResponse(b"<html><head><title>Mock Title</title></head></html>")

def test_task_func(monkeypatch):
    # Mock mechanize.Browser to use our MockBrowser
    monkeypatch.setattr(mechanize, 'Browser', MockBrowser)

    url = "http://example.com"
    form_id = 0
    data = {"field1": "value1", "field2": "value2"}

    result = task_func(url, form_id, data)

    assert result == "Mock Title"