python
import pytest
from src_0398 import task_func

def test_task_func():
    API_URL = 'https://httpbin.org/ip'
    ip_address = task_func(API_URL)
    assert isinstance(ip_address, str)
    assert re.match(r'[0-9]+(?:\.[0-9]+){3}', ip_address)