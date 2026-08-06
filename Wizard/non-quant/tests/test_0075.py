python
import socket
import requests
import pytest

def task_func(host):
    if not host:
        raise ValueError("Host must be a non-empty string.")

    try:
        # Fetch IP address
        ip_address = socket.gethostbyname(host)

        # Fetch geolocation
        response = requests.get(f"https://ipinfo.io/{ip_address}")
        response.raise_for_status()
        geolocation = response.json()

        return {
            'ip_address': ip_address,
            'geolocation': geolocation
        }
    except (socket.gaierror, requests.HTTPError) as e:
        raise ConnectionError(f"Failed to retrieve information for {host}: {e}")

def test_task_func():
    # Test with valid host
    assert task_func('example.com') == {
        'ip_address': '192.168.127.12',
        'geolocation': {
            'ip': '192.168.127.12',
            'city': 'San Francisco',
            'region': 'California',
            'country': 'US',
            'loc': '37.7749,-122.4194',
            'org': 'AS15169 Google Inc.',
            'postal': '94107'
        }
    }

    # Test with invalid host
    with pytest.raises(ConnectionError):
        task_func('')

    # Test with non-string host
    with pytest.raises(ValueError):
        task_func(123)