python
import re
import socket
import urllib.parse
import pytest

def task_func(myString):
    urls = re.findall(r'https?://[^\s,]+', myString)
    ip_addresses = {}

    for url in urls:
        domain = urllib.parse.urlparse(url).netloc
        try:
            ip_addresses[domain] = socket.gethostbyname(domain)
        except socket.gaierror:
            ip_addresses[domain] = None  # Handle domains that cannot be resolved

    return ip_addresses

def test_task_func():
    # Test case 1
    myString = "Check out this website: https://www.google.com and this one: http://www.yahoo.com"
    expected_output = {'www.google.com': '192.168.127.12', 'www.yahoo.com': '192.168.3.11'}
    assert task_func(myString) == expected_output

    # Test case 2
    myString = "Check out this website: https://www.google.com and this one: http://www.yahoo.com"
    expected_output = {'www.google.com': '192.168.127.12', 'www.yahoo.com': '192.168.3.11'}
    assert task_func(myString) == expected_output

    # Test case 3
    myString = "Check out this website: https://www.google.com and this one: http://www.yahoo.com"
    expected_output = {'www.google.com': '192.168.127.12', 'www.yahoo.com': '192.168.3.11'}
    assert task_func(myString) == expected_output