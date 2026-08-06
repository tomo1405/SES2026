import pytest
from src_0212 import task_func
import os
import zipfile
import tempfile

def test_task_func():
    # Create a temporary directory for testing
    with tempfile.TemporaryDirectory() as temp_dir:
        # URL of a sample zip file for testing
        url = "https://example.com/sample.zip"
        
        # Mock the requests.get call to return a fake response
        class MockResponse:
            def __init__(self, content):
                self.content = content
            
            def raise_for_status(self):
                pass
        
        # Sample zip file content (empty zip file)
        sample_zip_content = b'PK\x05\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        
        # Patch the requests.get method to return our mock response
        with pytest.MonkeyPatch.context() as mp:
            mp.setattr('requests.get', lambda url, headers: MockResponse(sample_zip_content))
            
            # Call the function
            result = task_func(url, temp_dir)
            
            # Check that the function returns the correct list of extracted files
            assert result == []
            
            # Check that the zip file was created and then removed
            zip_path = os.path.join(temp_dir, 'sample.zip')
            assert not os.path.exists(zip_path)
            
            # Check that the destination directory is empty after extraction
            assert os.listdir(temp_dir) == []

def test_task_func_with_headers():
    # Create a temporary directory for testing
    with tempfile.TemporaryDirectory() as temp_dir:
        # URL of a sample zip file for testing
        url = "https://example.com/sample.zip"
        
        # Custom headers
        headers = {
            'accept': 'application/zip',
            'Authorization': 'Bearer token'
        }
        
        # Mock the requests.get call to return a fake response
        class MockResponse:
            def __init__(self, content):
                self.content = content
            
            def raise_for_status(self):
                pass
        
        # Sample zip file content (empty zip file)
        sample_zip_content = b'PK\x05\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        
        # Patch the requests.get method to return our mock response
        with pytest.MonkeyPatch.context() as mp:
            mp.setattr('requests.get', lambda url, headers: MockResponse(sample_zip_content))
            
            # Call the function with custom headers
            result = task_func(url, temp_dir, headers=headers)
            
            # Check that the function returns the correct list of extracted files
            assert result == []
            
            # Check that the zip file was created and then removed
            zip_path = os.path.join(temp_dir, 'sample.zip')
            assert not os.path.exists(zip_path)
            
            # Check that the destination directory is empty after extraction
            assert os.listdir(temp_dir) == []