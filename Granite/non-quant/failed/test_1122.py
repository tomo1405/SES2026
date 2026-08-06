import re
import urllib.parse
import requests
import json
from unittest.mock import patch, MagicMock

def task_func(myString, API_KEY):
    urls = re.findall(r'(https?://[^\s,]+)', myString)
    geo_data = {}

    for url in urls:
        domain = urllib.parse.urlparse(url).netloc
        response = requests.get(f"http://ip-api.com/json/{domain}?access_key={API_KEY}")
        geo_data[domain] = json.loads(response.text)

    return geo_data

def test_task_func():
    with patch('urllib.parse.urlparse') as mock_urlparse, \
         patch('requests.get') as mock_get, \
         patch('json.loads') as mock_json_loads:

        mock_urlparse.return_value = MagicMock(netloc='example.com')
        mock_get.return_value = MagicMock(text='{"lat": 123, "lon": 456}')
        mock_json_loads.return_value = {'lat': 123, 'lon': 456}

        myString = 'https://example.com https://example.org'
        API_KEY = '123456'

        result = task_func(myString, API_KEY)

        assert result == {'example.com': {'lat': 123, 'lon': 456}, 'example.org': {'lat': 123, 'lon': 456}}