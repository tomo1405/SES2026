import os
import urllib

import pandas as pd
import pytest
from src_1001 import task_func


# Mocking urllib.request.urlretrieve to avoid actual file downloads
class MockUrlRetrieve:
    def __init__(self, url, filename):
        self.url = url
        self.filename = filename

    def __enter__(self):
        # Create a mock JSON file
        with open(self.filename, "w") as f:
            f.write('{"key": "value"}')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Clean up the mock JSON file
        os.remove(self.filename)

@pytest.fixture
def mock_urlretrieve(monkeypatch):
    monkeypatch.setattr(urllib.request, 'urlretrieve', MockUrlRetrieve)

def test_task_func(mock_urlretrieve):
    url = "http://example.com/data.json"
    df = task_func(url)

    # Check if the DataFrame is created correctly
    assert isinstance(df, pd.DataFrame)
    assert "key" in df.columns
    assert df.loc[0, "key"] == "value"

def test_task_func_file_cleanup(mock_urlretrieve):
    url = "http://example.com/data.json"
    task_func(url)

    # Check if the temporary file is cleaned up
    assert not os.path.exists("downloaded_file.json")