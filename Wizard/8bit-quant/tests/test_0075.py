python
import pytest
from src_0075 import task_func

def test_task_func():
    # Test valid input
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

    # Test invalid input
    with pytest.raises(ValueError):
        task_func('')

    with pytest.raises(ValueError):
        task_func(None)

    with pytest.raises(ConnectionError):
        task_func('invalid.host')