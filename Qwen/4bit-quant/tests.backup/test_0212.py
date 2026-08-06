import pytest
from src_0212 import task_func
import os
import tempfile
import shutil

@pytest.fixture
def setup_test_environment():
    # Create a temporary directory for testing
    temp_dir = tempfile.mkdtemp()
    yield temp_dir
    # Clean up the temporary directory after tests
    shutil.rmtree(temp_dir)

def test_task_func_with_valid_url(setup_test_environment):
    url = "https://example.com/sample.zip"
    destination_directory = setup_test_environment
    headers = {
        'accept': 'application/octet-stream'
    }
    
    # Mocking the requests.get to simulate a successful response
    def mock_get(url, headers):
        class MockResponse:
            def __init__(self, content):
                self.content = content
            
            def raise_for_status(self):
                pass
        
        # Simulate a zip file content
        with open("tests/data/sample.zip", "rb") as f:
            content = f.read()
        
        return MockResponse(content)
    
    requests.get = mock_get
    
    extracted_files = task_func(url, destination_directory, headers)
    
    assert isinstance(extracted_files, list)
    assert len(extracted_files) > 0
    assert all(isinstance(file, str) for file in extracted_files)

def test_task_func_without_headers(setup_test_environment):
    url = "https://example.com/sample.zip"
    destination_directory = setup_test_environment
    
    # Mocking the requests.get to simulate a successful response
    def mock_get(url, headers):
        class MockResponse:
            def __init__(self, content):
                self.content = content
            
            def raise_for_status(self):
                pass
        
        # Simulate a zip file content
        with open("tests/data/sample.zip", "rb") as f:
            content = f.read()
        
        return MockResponse(content)
    
    requests.get = mock_get
    
    extracted_files = task_func(url, destination_directory)
    
    assert isinstance(extracted_files, list)
    assert len(extracted_files) > 0
    assert all(isinstance(file, str) for file in extracted_files)

def test_task_func_with_invalid_url(setup_test_environment):
    url = "https://example.com/nonexistent.zip"
    destination_directory = setup_test_environment
    headers = {
        'accept': 'application/octet-stream'
    }
    
    # Mocking the requests.get to simulate a failed response
    def mock_get(url, headers):
        class MockResponse:
            def __init__(self, status_code):
                self.status_code = status_code
            
            def raise_for_status(self):
                raise requests.exceptions.HTTPError(f"HTTP {self.status_code}")
        
        return MockResponse(404)
    
    requests.get = mock_get
    
    with pytest.raises(requests.exceptions.HTTPError) as excinfo:
        task_func(url, destination_directory, headers)
    
    assert str(excinfo.value) == "HTTP 404"

def test_task_func_with_non_zip_file(setup_test_environment):
    url = "https://example.com/sample.txt"
    destination_directory = setup_test_environment
    headers = {
        'accept': 'text/plain'
    }
    
    # Mocking the requests.get to simulate a successful response with a non-zip file
    def mock_get(url, headers):
        class MockResponse:
            def __init__(self, content):
                self.content = content
            
            def raise_for_status(self):
                pass
        
        # Simulate a text file content
        content = b"This is a sample text file."
        
        return MockResponse(content)
    
    requests.get = mock_get
    
    with pytest.raises(zipfile.BadZipFile):
        task_func(url, destination_directory, headers)