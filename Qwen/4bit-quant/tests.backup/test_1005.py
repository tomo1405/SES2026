import pytest
from src_1005 import task_func
import matplotlib.pyplot as plt
import io
import urllib.error

# Mocking the urllib.request.urlopen to simulate HTTP responses
class MockResponse:
    def __init__(self, data):
        self.data = data

    def read(self):
        return self.data.encode()

    def close(self):
        pass

def test_task_func_valid_url(monkeypatch):
    # Mock the urlopen function to return a specific HTML content
    mock_html_content = "This is a test. This test is only a test."
    monkeypatch.setattr(urllib.request, 'urlopen', lambda url: MockResponse(mock_html_content))

    # Call the function with a dummy URL
    word_freq, ax = task_func("http://dummy.url")

    # Check the word frequency
    expected_word_freq = {'This': 2, 'is': 2, 'a': 1, 'test': 2, 'only': 1}
    assert word_freq == expected_word_freq

    # Check the plot properties
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == "Top 10 Most Common Words"
    assert ax.get_xlabel() == "Words"
    assert ax.get_ylabel() == "Frequency"

def test_task_func_invalid_url(monkeypatch):
    # Mock the urlopen function to raise an HTTPError
    def mock_urlopen(url):
        raise urllib.error.HTTPError(url, 404, "Not Found", None, None)

    monkeypatch.setattr(urllib.request, 'urlopen', mock_urlopen)

    # Call the function with a dummy URL that will raise an error
    with pytest.raises(urllib.error.HTTPError):
        task_func("http://invalid.url")

def test_task_func_empty_response(monkeypatch):
    # Mock the urlopen function to return an empty response
    monkeypatch.setattr(urllib.request, 'urlopen', lambda url: MockResponse(""))

    # Call the function with a dummy URL
    word_freq, ax = task_func("http://empty.url")

    # Check the word frequency
    assert word_freq == {}

    # Check the plot properties
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == "Top 10 Most Common Words"
    assert ax.get_xlabel() == "Words"
    assert ax.get_ylabel() == "Frequency"