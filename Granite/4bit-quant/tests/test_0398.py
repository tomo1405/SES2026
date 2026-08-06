import re
import urllib.request
import json
from src_0398 import task_func

def test_task_func_valid_ip():
    API_URL = "https://api.ipify.org"
    ip = task_func(API_URL)
    assert re.match(r'[0-9]+(?:\.[0-9]+){3}', ip)

def test_task_func_invalid_ip():
    API_URL = "https://api.example.com"
    ip = task_func(API_URL)
    assert ip == "Invalid IP address received"

def test_task_func_exception():
    API_URL = "https://api.example.com"
    ip = task_func(API_URL)
    assert isinstance(ip, str) and "Exception" in ip