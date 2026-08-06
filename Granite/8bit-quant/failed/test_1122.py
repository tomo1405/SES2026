import pytest
from src_1122 import task_func

def test_task_func():
    myString = "https://www.google.com https://www.facebook.com"
    API_KEY = "your_api_key"
    expected_output = {
        "www.google.com": {"country": "United States", "city": "Mountain View", "zip": "94043", "latitude": 37.405991, "longitude": -122.078519},
        "www.facebook.com": {"country": "United States", "city": "Menlo Park", "zip": "94025", "latitude": 37.485991, "longitude": -122.158519}
    }
    actual_output = task_func(myString, API_KEY)
    assert actual_output == expected_output

def test_task_func_with_invalid_api_key():
    myString = "https://www.google.com https://www.facebook.com"
    API_KEY = "invalid_api_key"
    with pytest.raises(requests.exceptions.HTTPError):
        task_func(myString, API_KEY)