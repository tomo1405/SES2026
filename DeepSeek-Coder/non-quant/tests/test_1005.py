import pytest
from src_1005 import task_func
import urllib.request
import re
from collections import Counter
import matplotlib.pyplot as plt

@pytest.fixture
def mock_urlopen(monkeypatch):
    def mock_urlopen(url):
        class MockResponse:
            def read(self):
                return b"This is a test text. This text is for testing."

            def readline(self):
                return b"This is a test text. This text is for testing."

        return MockResponse()

    monkeypatch.setattr(urllib.request, 'urlopen', mock_urlopen)

def test_task_func(monkeypatch):
    mock_urlopen(monkeypatch)
    result = task_func("http://example.com")
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert isinstance(result[0], Counter)
    assert isinstance(result[1], plt.Axes)