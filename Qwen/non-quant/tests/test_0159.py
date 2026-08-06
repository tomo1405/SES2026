import gzip
import json
import os
import urllib

import pytest
from src_0159 import task_func


def test_task_func(tmpdir):
    # Mock the urllib.request.urlopen to return a dummy JSON response
    class MockResponse:
        def __init__(self, data):
            self.data = data

        def read(self):
            return self.data.encode()

    url_str = "http://example.com/api"
    dummy_json = {"key": "value"}
    mock_response = MockResponse(json.dumps(dummy_json))

    # Patch urllib.request.urlopen to use the mock response
    with pytest.MonkeyPatch.context() as mp:
        mp.setattr(urllib.request, 'urlopen', lambda x: mock_response)
        
        # Define a temporary file path
        file_path = str(tmpdir / "test_output.json.gz")
        
        # Call the function
        result = task_func(url_str, file_path)
        
        # Check if the function returns the correct file path
        assert result == file_path
        
        # Check if the file exists
        assert os.path.exists(file_path)
        
        # Read and decompress the file to verify its contents
        with gzip.open(file_path, 'rb') as f_in:
            content = f_in.read().decode()
        
        # Parse the JSON content
        parsed_content = json.loads(content)
        
        # Check if the content matches the expected JSON
        assert parsed_content == dummy_json