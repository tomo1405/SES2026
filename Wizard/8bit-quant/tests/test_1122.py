python
import re
import urllib.parse
import requests
import json
import pytest

def task_func(myString, API_KEY):
    urls = re.findall(r'(https?://[^\s,]+)', myString)
    geo_data = {}

    for url in urls:
        domain = urllib.parse.urlparse(url).netloc
        response = requests.get(f"http://ip-api.com/json/{domain}?access_key={API_KEY}")
        geo_data[domain] = json.loads(response.text)

    return geo_data

def test_task_func():
    myString = "Check out this website: https://www.google.com and this one: http://www.yahoo.com"
    API_KEY = "your_api_key_here"
    expected_geo_data = {
        "www.google.com": {"status": "success", "country": "United States", "regionName": "California", "city": "Mountain View", "zip": "94043", "lat": 37.4229, "lon": -122.085, "timezone": "America/Los_Angeles", "isp": "Google LLC", "org": "Google Public DNS", "as": "AS15169 Google LLC", "query": "172.217.160.100"},
        "www.yahoo.com": {"status": "success", "country": "United States", "regionName": "California", "city": "Mountain View", "zip": "94043", "lat": 37.4229, "lon": -122.085, "timezone": "America/Los_Angeles", "isp": "Yahoo! Inc.", "org": "Level 3 Communications", "as": "AS15169 Yahoo! Inc.", "query": "172.217.160.100"}
    }
    geo_data = task_func(myString, API_KEY)
    assert geo_data == expected_geo_data