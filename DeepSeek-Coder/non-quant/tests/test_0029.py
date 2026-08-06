import pytest
from src_0029 import task_func
import requests
import json
import base64

def test_task_func():
    # Mock the requests.post response
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    # Test case 1: Successful API call
    requests.post = lambda url, json_data: MockResponse({'status': 'success', 'data': 'expected_data'}, 200)
    result = task_func({'key': 'value'})
    assert result == {'status': 'success', 'data': 'expected_data'}

    # Test case 2: API call with error
    requests.post = lambda url, json_data: MockResponse({'status': 'error', 'message': 'API error'}, 500)
    with pytest.raises(Exception) as exc_info:
        task_func({'key': 'value'})
    assert str(exc_info.value) == 'API error: API error'