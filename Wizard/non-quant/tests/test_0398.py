python
import re
import urllib.request
import json

# Constants
IP_REGEX = r'[0-9]+(?:\.[0-9]+){3}'

def test_task_func():
    API_URL = 'https://api.ipify.org?format=json'
    response = urllib.request.urlopen(API_URL)
    data = json.loads(response.read())
    ip = data['ip']
    assert re.match(IP_REGEX, ip)

def test_task_func_invalid_url():
    API_URL = 'https://invalid.url'
    response = urllib.request.urlopen(API_URL)
    assert response.status == 404

def test_task_func_invalid_ip():
    API_URL = 'https://api.ipify.org?format=json'
    response = urllib.request.urlopen(API_URL)
    data = json.loads(response.read())
    ip = data['ip']
    assert not re.match(IP_REGEX, ip)