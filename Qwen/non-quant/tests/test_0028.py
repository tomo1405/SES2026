import pytest
from src_0028 import task_func
import json
import base64
from datetime import datetime

def test_task_func():
    # Sample input data
    input_data = {'key': 'value'}
    
    # Expected output structure
    expected_output_structure = {
        'key': 'value',
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    # Call the function
    result = task_func(input_data)
    
    # Decode the result to check its contents
    decoded_result = json.loads(base64.b64decode(result).decode('ascii'))
    
    # Check if the decoded result contains the correct key-value pair
    assert decoded_result['key'] == 'value'
    
    # Check if the timestamp is present and in the correct format
    assert 'timestamp' in decoded_result
    assert datetime.strptime(decoded_result['timestamp'], "%Y-%m-%d %H:%M:%S")

def test_task_func_with_custom_date_format():
    # Sample input data
    input_data = {'key': 'value'}
    
    # Custom date format
    custom_date_format = "%Y-%m-%d"
    
    # Expected output structure
    expected_output_structure = {
        'key': 'value',
        'timestamp': datetime.now().strftime(custom_date_format)
    }
    
    # Call the function with custom date format
    result = task_func(input_data, DATE_FORMAT=custom_date_format)
    
    # Decode the result to check its contents
    decoded_result = json.loads(base64.b64decode(result).decode('ascii'))
    
    # Check if the decoded result contains the correct key-value pair
    assert decoded_result['key'] == 'value'
    
    # Check if the timestamp is present and in the correct format
    assert 'timestamp' in decoded_result
    assert datetime.strptime(decoded_result['timestamp'], custom_date_format)