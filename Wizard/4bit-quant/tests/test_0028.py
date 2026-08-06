python
import json
import base64
from datetime import datetime
import pytest

def task_func(data: dict, DATE_FORMAT = "%Y-%m-%d %H:%M:%S") -> str:
    # Adding current timestamp to the dictionary
    data['timestamp'] = datetime.now().strftime(DATE_FORMAT)
    
    # Encoding the dictionary to a JSON-formatted string and then encoding it in ASCII using base64 encoding
    json_data = json.dumps(data)
    encoded_data = base64.b64encode(json_data.encode('ascii')).decode('ascii')
    
    return encoded_data

def test_task_func():
    # Test case 1: Valid input data
    data = {'name': 'John', 'age': 30}
    encoded_data = task_func(data)
    assert isinstance(encoded_data, str)
    assert len(encoded_data) > 0
    
    # Test case 2: Invalid input data (not a dictionary)
    data = 'not a dictionary'
    with pytest.raises(TypeError):
        task_func(data)
    
    # Test case 3: Invalid input data (missing required key)
    data = {'name': 'John'}
    with pytest.raises(KeyError):
        task_func(data)
    
    # Test case 4: Invalid input data (invalid value type)
    data = {'name': 'John', 'age': '30'}
    with pytest.raises(TypeError):
        task_func(data)