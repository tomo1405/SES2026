import pytest
from src_1121 import task_func

def test_task_func():
    myString = "https://www.example.com, https://www.example.org"
    API_KEY = "your_api_key"
    expected_output = {
        "www.example.com": {
            "country": "United States",
            "countryCode": "US",
            "region": "California",
            "regionName": "California",
            "city": "Mountain View",
            "zip": "94043",
            "lat": 37.4192,
            "lon": -122.0574,
            "timezone": "America/Los_Angeles",
            "isp": "Google LLC",
            "org": "Google Public DNS",
            "as": "AS15169 Google LLC",
            "asname": "GOOGLE",
            "reverse": "cpe-192-168-1-1.nyc.res.rr.com",
            "mobile": False,
            "proxy": False,
            "hosting": False,
            "query": "www.example.com"
        },
        "www.example.org": {
            "country": "United States",
            "countryCode": "US",
            "region": "California",
            "regionName": "California",
            "city": "Mountain View",
            "zip": "94043",
            "lat": 37.4192,
            "lon": -122.0574,
            "timezone": "America/Los_Angeles",
            "isp": "Google LLC",
            "org": "Google Public DNS",
            "as": "AS15169 Google LLC",
            "asname": "GOOGLE",
            "reverse": "cpe-192-168-1-1.nyc.res.rr.com",
            "mobile": False,
            "proxy": False,
            "hosting": False,
            "query": "www.example.org"
        }
    }
    assert task_func(myString, API_KEY) == expected_output