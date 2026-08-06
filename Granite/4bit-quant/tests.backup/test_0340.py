import json
import urllib.parse
import hmac
import hashlib
import pytest

from src_0340 import task_func

def test_task_func():
    req_data = {"key1": "value1", "key2": "value2"}
    secret_key = "my_secret_key"

    with pytest.raises(TypeError):
        task_func(123, secret_key)  # Test if TypeError is raised when req_data is not a dictionary

    url_encoded_signature = task_func(req_data, secret_key)

    assert isinstance(url_encoded_signature, str)  # Test if the returned value is a string

    # You can add more test cases here to cover different scenarios