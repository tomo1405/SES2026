import pytest
from src_0413 import task_func

# Mocking the file operations and JSON content for testing
class MockFile:
    def __init__(self, content):
        self.content = content

    def read(self):
        return self.content

def test_task_func_with_valid_json():
    # Prepare a mock JSON file content
    json_content = '{"key1": "SGVsbG8gV29ybGQh"}'  # Base64 encoded "Hello World!"
    mock_file = MockFile(json_content)
    
    # Patch the open function to return our mock file
    with pytest.monkeypatch.context() as mp:
        mp.setattr('builtins.open', lambda _, __: mock_file)
        
        # Call the function
        result = task_func('dummy_path.json')
        
        # Assert the result
        assert result == {'key1': 'Hello World!'}

def test_task_func_with_invalid_json():
    # Prepare a mock JSON file content with invalid base64
    json_content = '{"key1": "invalid_base64"}'
    mock_file = MockFile(json_content)
    
    # Patch the open function to return our mock file
    with pytest.monkeypatch.context() as mp:
        mp.setattr('builtins.open', lambda _, __: mock_file)
        
        # Call the function and expect an exception
        with pytest.raises(base64.binascii.Error):
            task_func('dummy_path.json')

def test_task_func_with_nonexistent_file():
    # Test case for when the file does not exist
    with pytest.raises(FileNotFoundError):
        task_func('nonexistent_file.json')