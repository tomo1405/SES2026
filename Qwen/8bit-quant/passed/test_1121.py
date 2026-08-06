import pytest
from src_1121 import task_func
import requests
import json

# Mocking the requests.get function to simulate API responses
class MockResponse:
    def __init__(self, text):
        self.text = text

def mock_requests_get(*args, **kwargs):
    # Simulate a successful response with dummy data
    if 'ip-api.com/json/' in args[0]:
        return MockResponse(json.dumps({
            "status": "success",
            "country": "CountryName",
            "regionName": "RegionName",
            "city": "CityName",
            "zip": "ZipCode",
            "lat": 123.456,
            "lon": -78.901,
            "timezone": "TimeZone",
            "isp": "ISPName",
            "org": "OrgName",
            "as": "ASName"
        }))
    else:
        raise Exception("Unexpected URL")

@pytest.fixture(autouse=True)
def mock_requests(monkeypatch):
    monkeypatch.setattr(requests, 'get', mock_requests_get)

def test_task_func_with_valid_input():
    myString = "Check out these websites: https://example.com and http://testsite.org"
    API_KEY = "dummy_api_key"
    expected_output = {
        "example.com": {
            "status": "success",
            "country": "CountryName",
            "regionName": "RegionName",
            "city": "CityName",
            "zip": "ZipCode",
            "lat": 123.456,
            "lon": -78.901,
            "timezone": "TimeZone",
            "isp": "ISPName",
            "org": "OrgName",
            "as": "ASName"
        },
        "testsite.org": {
            "status": "success",
            "country": "CountryName",
            "regionName": "RegionName",
            "city": "CityName",
            "zip": "ZipCode",
            "lat": 123.456,
            "lon": -78.901,
            "timezone": "TimeZone",
            "isp": "ISPName",
            "org": "OrgName",
            "as": "ASName"
        }
    }
    assert task_func(myString, API_KEY) == expected_output

def test_task_func_with_no_urls():
    myString = "No URLs here!"
    API_KEY = "dummy_api_key"
    expected_output = {}
    assert task_func(myString, API_KEY) == expected_output

def test_task_func_with_invalid_url():
    myString = "Invalid URL: ftp://example.com"
    API_KEY = "dummy_api_key"
    expected_output = {}
    assert task_func(myString, API_KEY) == expected_output