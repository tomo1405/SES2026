python
import json
import urllib.parse
import hmac
import hashlib

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
    # Test case 1: Valid request data and secret key
    req_data = {"name": "John Doe", "age": 30}
    secret_key = "my_secret_key"
    expected_signature = "1c7d5d5d1d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d"
    assert task_func(req_data, secret_key) == expected_signature

    # Test case 2: Invalid request data type
    req_data = "not a dictionary"
    secret_key = "my_secret_key"
    with pytest.raises(TypeError):
        task_func(req_data, secret_key)

    # Test case 3: Invalid secret key type
    req_data = {"name": "John Doe", "age": 30}
    secret_key = 12345
    with pytest.raises(TypeError):
        task_func(req_data, secret_key)