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
    # Test case 1: Test with a simple dictionary
    data = {'name': 'John', 'age': 30}
    expected_output = 'eyJuYW1lIjogIkpvaG4iLCAiYWdlIjogMzAsICJ0aW1lc3RhbXAiOiAiMjAxOC0wMy0xMFQyMToyMToyMC4yMzhaIiwidGltZXN0YW1wIjogIjIwMTgtMDMtMTBUMjE6MjE6MjAuMTYyWiJ9'
    assert task_func(data) == expected_output
    
    # Test case 2: Test with a dictionary containing nested dictionaries
    data = {'name': 'John', 'age': 30, 'address': {'street': '123 Main St', 'city': 'Anytown', 'state': 'CA', 'zip': '12345'}}
    expected_output = 'eyJuYW1lIjogIkpvaG4iLCAiYWdlIjogMzAsICJ0aW1lc3RhbXAiOiAiMjAxOC0wMy0xMFQyMToyMToyMC4yMzhaIiwiaW50ZXJuYWwiOiB7InN0cm9rZSI6ICIxMjMgTWFpbCBUcyIsICJjaXR5IjogIkFueXRvcnRvd24iLCAic3RhdHVzIjogIkNBIiwgInppcCI6ICIxMjM0NTY3ODkiXX0='
    assert task_func(data) == expected_output
    
    # Test case 3: Test with a dictionary containing a list of dictionaries
    data = {'name': 'John', 'age': 30, 'hobbies': [{'name': 'reading', 'rating': 5}, {'name': 'swimming', 'rating': 4}]}
    expected_output = 'eyJuYW1lIjogIkpvaG4iLCAiYWdlIjogMzAsICJoaG9iaXplcyI6IHsNCiAgICJuYW1lIjogInJlYWRpbmcifSwgICAgInJhdGlvIjogNiwNCiAgICB7Im5hbWUiOiAic3dpbW1pbmcifSwgICAgInJhdGlvIjogNCwNCiAgfQp9'
    assert task_func(data) == expected_output