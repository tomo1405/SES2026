python
import re
import urllib.parse
import ssl
import socket
import pytest

def task_func(myString):
    urls = re.findall(r'https://[^\s,]+', myString)
    ssl_expiry_dates = {}

    for url in urls:
        try:
            domain = urllib.parse.urlparse(url).netloc
            context = ssl.create_default_context()
            with socket.create_connection((domain, 443)) as sock:
                with context.wrap_socket(sock, server_hostname=domain) as ssock:
                    ssl_expiry_dates[domain] = ssock.getpeercert()['notAfter']
        except ssl.SSLError:
            continue  # Ignore SSL errors or log them if necessary

    return ssl_expiry_dates

def test_task_func():
    myString = "Here are some URLs: https://www.google.com, https://www.facebook.com, https://www.twitter.com"
    expected_output = {'www.google.com': '20220518000000Z', 'www.facebook.com': '20220518000000Z', 'www.twitter.com': '20220518000000Z'}
    assert task_func(myString) == expected_output