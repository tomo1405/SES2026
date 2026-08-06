import re
import urllib.request
import json
from src_0398 import task_func
import pytest

# Constants
IP_REGEX = r'[0-9]+(?:\.[0-9]+){3}'

def test_task_func_valid_ip():
    API_URL = "https://api.ipify.org"
    ip = task_func(API_URL)
    assert re.match(IP_REGEX, ip)

def test_task_func_invalid_ip():
    API_URL = "https://api.example.com"
    ip = task_func(API_URL)
    assert ip == "Invalid IP address received"

def test_task_func_exception():
    API_URL = "https://api.example.com"
    with pytest.raises(Exception) as e:
        task_func(API_URL)
    assert str(e.value) == "Some error message"