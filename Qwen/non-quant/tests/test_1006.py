import os
import tempfile
import urllib
import zipfile

import pytest
from src_1006 import task_func


@pytest.fixture
def temp_dir():
    with tempfile.TemporaryDirectory() as tmpdir:
        yield tmpdir

@pytest.fixture
def sample_zip_file(temp_dir):
    zip_path = os.path.join(temp_dir, "sample.zip")
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        zipf.writestr('testfile.txt', 'Hello, World!')
    return zip_path

@pytest.fixture
def mock_url(sample_zip_file):
    class MockResponse:
        def __init__(self, filename):
            self.filename = filename

        def read(self):
            with open(self.filename, 'rb') as f:
                return f.read()

    def mock_urlopen(url):
        return MockResponse(sample_zip_file)

    return mock_url

def test_task_func(monkeypatch, temp_dir, mock_url):
    monkeypatch.setattr(urllib.request, 'urlopen', mock_url)
    url = "http://example.com/sample.zip"
    save_path = os.path.join(temp_dir, "downloaded_file.zip")
    extract_path = os.path.join(temp_dir, "extracted_files")

    result = task_func(url, save_path, extract_path)

    assert result == extract_path
    assert os.path.exists(extract_path)
    assert os.path.exists(os.path.join(extract_path, "testfile.txt"))
    assert not os.path.exists(save_path)

def test_task_func_url_error(monkeypatch, temp_dir):
    def mock_urlopen(url):
        raise urllib.error.URLError("Test URLError")

    monkeypatch.setattr(urllib.request, 'urlopen', mock_urlopen)
    url = "http://example.com/sample.zip"
    save_path = os.path.join(temp_dir, "downloaded_file.zip")
    extract_path = os.path.join(temp_dir, "extracted_files")

    result = task_func(url, save_path, extract_path)

    assert result == "URL Error: Test URLError"
    assert not os.path.exists(save_path)
    assert not os.path.exists(extract_path)