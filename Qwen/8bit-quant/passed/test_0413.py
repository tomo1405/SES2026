import pytest
from src_0413 import task_func
import json
import base64
import unicodedata

# Helper function to create a temporary JSON file for testing
def create_temp_json(data, tmp_path):
    json_file = tmp_path / "test.json"
    with open(json_file, 'w') as f:
        json.dump(data, f)
    return json_file

def test_task_func(tmp_path):
    # Test data
    test_data = {
        "key1": base64.b64encode("value1".encode('utf-8')).decode('utf-8'),
        "key2": base64.b64encode("value2".encode('utf-8')).decode('utf-8')
    }
    
    # Create a temporary JSON file
    json_file = create_temp_json(test_data, tmp_path)
    
    # Expected result after decoding
    expected_result = {
        "key1": unicodedata.normalize('NFC', "value1"),
        "key2": unicodedata.normalize('NFC', "value2")
    }
    
    # Run the function
    result = task_func(str(json_file))
    
    # Assert the result
    assert result == expected_result

def test_task_func_with_unicode(tmp_path):
    # Test data with unicode characters
    test_data = {
        "key1": base64.b64encode("café".encode('utf-8')).decode('utf-8'),
        "key2": base64.b64encode("naïve".encode('utf-8')).decode('utf-8')
    }
    
    # Create a temporary JSON file
    json_file = create_temp_json(test_data, tmp_path)
    
    # Expected result after decoding and normalization
    expected_result = {
        "key1": unicodedata.normalize('NFC', "café"),
        "key2": unicodedata.normalize('NFC', "naïve")
    }
    
    # Run the function
    result = task_func(str(json_file))
    
    # Assert the result
    assert result == expected_result

def test_task_func_empty_file(tmp_path):
    # Empty test data
    test_data = {}
    
    # Create a temporary JSON file
    json_file = create_temp_json(test_data, tmp_path)
    
    # Expected result after decoding
    expected_result = {}
    
    # Run the function
    result = task_func(str(json_file))
    
    # Assert the result
    assert result == expected_result