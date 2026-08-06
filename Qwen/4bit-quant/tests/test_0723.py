import os
import urllib

from src_0723 import task_func


# Mocking urllib.request.urlretrieve to avoid actual file downloads
class MockUrlRetrieve:
    def __init__(self, content):
        self.content = content

    def __call__(self, url, filename):
        with open(filename, 'w') as f:
            f.write(self.content)

def test_task_func(monkeypatch):
    # Mock the urlretrieve function to return a predefined content
    mock_content = "This is an ERROR message. There is another ERROR here."
    monkeypatch.setattr(urllib.request, 'urlretrieve', MockUrlRetrieve(mock_content))

    # Define the URL (it won't be actually used due to mocking)
    url = "http://example.com"

    # Call the function
    result = task_func(url)

    # Assert that the function returns the correct number of occurrences
    assert result == 2

def test_task_func_no_errors(monkeypatch):
    # Mock the urlretrieve function to return a predefined content without errors
    mock_content = "This is a normal message. No errors here."
    monkeypatch.setattr(urllib.request, 'urlretrieve', MockUrlRetrieve(mock_content))

    # Define the URL (it won't be actually used due to mocking)
    url = "http://example.com"

    # Call the function
    result = task_func(url)

    # Assert that the function returns the correct number of occurrences
    assert result == 0

def test_task_func_file_cleanup(monkeypatch):
    # Mock the urlretrieve function to return a predefined content
    mock_content = "This is an ERROR message."
    monkeypatch.setattr(urllib.request, 'urlretrieve', MockUrlRetrieve(mock_content))

    # Define the URL (it won't be actually used due to mocking)
    url = "http://example.com"

    # Call the function
    task_func(url)

    # Assert that the target file is cleaned up
    assert not os.path.exists('downloaded_file.txt')