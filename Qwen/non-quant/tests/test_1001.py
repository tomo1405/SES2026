import os
import urllib

import pandas as pd
import pytest
from src_1001 import task_func


# Mocking the urllib.request.urlretrieve function
class MockUrlRetrieve:
    def __init__(self, file_content):
        self.file_content = file_content

    def __call__(self, url, filename):
        with open(filename, "w") as f:
            f.write(self.file_content)

@pytest.fixture(autouse=True)
def mock_urlretrieve(monkeypatch):
    # Define the mock content of the JSON file
    mock_json_content = '{"name": "John", "age": 30}'
    
    # Create an instance of the mock class
    mock_url_retrieve_instance = MockUrlRetrieve(mock_json_content)
    
    # Patch the urllib.request.urlretrieve function
    monkeypatch.setattr(urllib.request, 'urlretrieve', mock_url_retrieve_instance)

def test_task_func():
    # Define a mock URL
    mock_url = "http://example.com/data.json"
    
    # Call the function with the mock URL
    result_df = task_func(mock_url)
    
    # Check if the DataFrame is created correctly
    expected_df = pd.DataFrame({"name": ["John"], "age": [30]})
    pd.testing.assert_frame_equal(result_df, expected_df)
    
    # Check if the temporary file is removed
    assert not os.path.exists("downloaded_file.json")