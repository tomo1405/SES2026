import pytest
from src_0028 import task_func
import json
import base64
from datetime import datetime

def test_task_func():
    # Test data
    data = {
        "key1": "value1",
        "key2": "value2"
    }
    
    # Call the function
    result = task_func(data)
    
    # Check the result
    assert isinstance(result, str), "The result should be a string"
    
    # Decode the result to verify
    decoded_result = base64.b64decode(result.encode('ascii')).decode('ascii')
    decoded_data = json.loads(decoded_result)
    
    # Check if the timestamp is added
    assert 'timestamp' in decoded_data, "Timestamp is not added to the data"
    assert isinstance(decoded_data['timestamp'], str), "Timestamp should be a string"
    
    # Check if the data is correctly encoded
    assert decoded_data['key1'] == "value1", "The data is not correctly encoded"