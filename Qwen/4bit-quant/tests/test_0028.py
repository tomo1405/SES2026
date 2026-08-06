import base64
import json
from datetime import datetime

import pytest
from src_0028 import task_func


def test_task_func():
    # Sample input data
    input_data = {'key': 'value'}
    
    # Call the function
    result = task_func(input_data)
    
    # Decode the base64 encoded string to get the JSON string
    decoded_json = base64.b64decode(result).decode('ascii')
    
    # Convert the JSON string back to a dictionary
    decoded_data = json.loads(decoded_json)
    
    # Check if the original data is present
    assert decoded_data['key'] == 'value'
    
    # Check if the timestamp key is added
    assert 'timestamp' in decoded_data
    
    # Check if the timestamp is in the correct format
    try:
        datetime.strptime(decoded_data['timestamp'], "%Y-%m-%d %H:%M:%S")
    except ValueError:
        pytest.fail("Timestamp is not in the correct format")