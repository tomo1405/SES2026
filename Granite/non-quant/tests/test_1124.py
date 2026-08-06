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
    myString = "Here are some URLs: https://www.example.com and https://www.google.com"
    expected_output = {'www.example.com': 'Not After: ...', 'www.google.com': 'Not After: ...'}
    actual_output = task_func(myString)
    assert actual_output == expected_output, "Expected output does not match actual output"

if __name__ == "__main__":
    pytest.main()