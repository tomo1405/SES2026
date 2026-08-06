import pytest
from src_0579 import task_func
import requests

def test_task_func_success():
    # Mock a successful response
    class MockResponse:
        def __init__(self, status_code, json_data):
            self.status_code = status_code
            self.json_data = json_data

        def json(self):
            return self.json_data

        def raise_for_status(self):
            return None

    # Mock data
    mock_data = {
        'name': 'John Doe',
        'email': 'john.doe@example.com'
    }
    mock_response = MockResponse(200, mock_data)

    with requests.get.return_value = mock_response

    result = task_func('testuser')

    assert result == mock_data

def test_task_func_failure():
    # Mock a failed response
    class MockResponse:
        def __init__(self, status_code):
            self.status_code = status_code

        def raise_for_status(self):
            raise requests.HTTPError("Mocked HTTP Error")

    mock_response = MockResponse(404)

    with pytest.raises(Exception):
        task_func('testuser')