python
import re
import socket
import urllib.parse

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
    myString = "This is a test string with https://www.google.com and http://www.yahoo.com"
    expected_output = {'www.google.com': '172.217.160.16', 'www.yahoo.com': '192.168.3.11'}
    assert task_func(myString) == expected_output

    # Test case 2
    myString = "This is a test string with https://www.google.com and http://www.yahoo.com and https://www.python.org"
    expected_output = {'www.google.com': '172.217.160.16', 'www.yahoo.com': '192.168.3.11', 'www.python.org': None}
    assert task_func(myString) == expected_output

    # Test case 3
    myString = "This is a test string with https://www.google.com and http://www.yahoo.com and https://www.python.org and https://www.github.com"
    expected_output = {'www.google.com': '172.217.160.16', 'www.yahoo.com': '192.168.3.11', 'www.python.org': None, 'www.github.com': None}
    assert task_func(myString) == expected_output