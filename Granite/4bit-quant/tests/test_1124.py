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
    myString = "Here are some URLs: https://www.google.com https://www.microsoft.com https://www.amazon.com"
    expected_output = {'www.google.com': 'Feb 20 14:23:03 2023', 'www.microsoft.com': 'Feb 20 14:23:03 2023', 'www.amazon.com': 'Feb 20 14:23:03 2023'}
    actual_output = task_func(myString)
    assert actual_output == expected_output, "Expected output does not match actual output"

if __name__ == "__main__":
    pytest.main()