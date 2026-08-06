python
import json
import urllib.parse
import hmac
import hashlib
import pytest

def task_func(req_data, secret_key):
    if not isinstance(req_data, dict):
        raise TypeError("req_data must be a dictionary")
    # Convert request data to json string
    json_req_data = json.dumps(req_data)
    # Create a new hmac object with the secret key and the json string as the message
    hmac_obj = hmac.new(secret_key.encode(), json_req_data.encode(), hashlib.sha256)
    # Get the hmac signature
    hmac_signature = hmac_obj.hexdigest()  # Use hexdigest for a hexadecimal representation
    # URL encode the hmac signature
    url_encoded_signature = urllib.parse.quote_plus(hmac_signature)

    return url_encoded_signature

def test_task_func():
    # Test case 1: Valid input
    req_data = {"key1": "value1", "key2": "value2"}
    secret_key = "secret_key"
    expected_output = "a7d1d8d5a5a6d5d96a8d5c2a96a6a95b99a7d1d8d5a5a6d5d96a8d5c2a96a6a95b99"
    assert task_func(req_data, secret_key) == expected_output

    # Test case 2: Invalid input (req_data is not a dictionary)
    req_data = "not a dictionary"
    secret_key = "secret_key"
    with pytest.raises(TypeError):
        task_func(req_data, secret_key)

    # Test case 3: Invalid input (secret_key is None)
    req_data = {"key1": "value1", "key2": "value2"}
    secret_key = None
    with pytest.raises(TypeError):
        task_func(req_data, secret_key)