import pytest
from src_0028 import task_func
import json
import base64
from datetime import datetime

def test_task_func():
    # Test with an empty dictionary
    input_data = {}
    result = task_func(input_data)
    decoded_result = base64.b64decode(result).decode('ascii')
    decoded_dict = json.loads(decoded_result)
    
    assert isinstance(decoded_dict['timestamp'], str)
    assert datetime.strptime(decoded_dict['timestamp'], "%Y-%m-%d %H:%M:%S")
    assert decoded_dict == {'timestamp': decoded_dict['timestamp']}
    
    # Test with a non-empty dictionary
    input_data = {'key': 'value'}
    result = task_func(input_data)
    decoded_result = base64.b64decode(result).decode('ascii')
    decoded_dict = json.loads(decoded_result)
    
    assert isinstance(decoded_dict['timestamp'], str)
    assert datetime.strptime(decoded_dict['timestamp'], "%Y-%m-%d %H:%M:%S")
    assert decoded_dict == {'key': 'value', 'timestamp': decoded_dict['timestamp']}
    
    # Test with a different date format
    input_data = {}
    result = task_func(input_data, DATE_FORMAT="%d-%m-%Y %H:%M:%S")
    decoded_result = base64.b64decode(result).decode('ascii')
    decoded_dict = json.loads(decoded_result)
    
    assert isinstance(decoded_dict['timestamp'], str)
    assert datetime.strptime(decoded_dict['timestamp'], "%d-%m-%Y %H:%M:%S")
    assert decoded_dict == {'timestamp': decoded_dict['timestamp']}