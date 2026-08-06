import json
import os
import tempfile

import pytest
import requests
from src_1138 import task_func


@pytest.fixture
def sample_html_file():
    fd, path = tempfile.mkstemp(suffix='.html')
    with os.fdopen(fd, 'w') as tmp:
        tmp.write('<html><body><p>Contact us at +1 800-555-0199 or +44 20 7946 0958</p></body></html>')
    yield path
    os.remove(path)

@pytest.fixture
def sample_output_file():
    fd, path = tempfile.mkstemp(suffix='.json')
    os.close(fd)
    yield path
    os.remove(path)

def test_task_func_with_local_file(sample_html_file, sample_output_file):
    url = f"file://{sample_html_file}"
    expected_output = ['+1 800-555-0199', '+44 20 7946 0958']
    result = task_func(url, sample_output_file)
    assert result == expected_output
    with open(sample_output_file, 'r') as f:
        saved_output = json.load(f)
    assert saved_output == expected_output

def test_task_func_with_remote_url(sample_output_file, monkeypatch):
    class MockResponse:
        def __init__(self, text):
            self.text = text

    def mock_get(url, headers):
        return MockResponse('<html><body><p>Contact us at +1 800-555-0199 or +44 20 7946 0958</p></body></html>')

    monkeypatch.setattr(requests, 'get', mock_get)
    url = "http://example.com"
    expected_output = ['+1 800-555-0199', '+44 20 7946 0958']
    result = task_func(url, sample_output_file)
    assert result == expected_output
    with open(sample_output_file, 'r') as f:
        saved_output = json.load(f)
    assert saved_output == expected_output

def test_task_func_no_phone_numbers(sample_output_file):
    url = f"file://{tempfile.NamedTemporaryFile(delete=False, mode='w').name}"
    expected_output = []
    result = task_func(url, sample_output_file)
    assert result == expected_output
    with open(sample_output_file, 'r') as f:
        saved_output = json.load(f)
    assert saved_output == expected_output